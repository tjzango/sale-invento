# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages

from sale.forms import OrderSaveForm, QuantityForm, DebtForm
from cart.cart import Cart
from store.models import Item, RequestOrder
from sale.models import Order, OrderItem
from index.models import Account


# Create your views here.
@login_required
def index(request):
    """
    This view is responsible for loading the sale.html file
    :param request:
    :return:
    """
    sales = OrderItem.objects.all()
    order = Order.objects.all()
    total_amount_made = sum(item.amount_paid for item in order)
    for item in sales:
        price = item.price * item.order.amount_paid
    context = {
        'sales': sales,
        'total': sales.count(),
        'total_amount_made': total_amount_made
    }
    return render(request, 'sale.html', context)


@login_required
def new_sale(request):
    """
    This view is responsible for allowing users making new sale
    :param request:
    :return request, new_sale.html, context{form, items}:
    """
    cart = Cart(request)
    order_form = OrderSaveForm(request.POST or None)
    if order_form.is_valid():
        order = order_form.save(commit=False)
        cash = order_form.cleaned_data.get('cash_paid')
        bank = order_form.cleaned_data.get('bank_paid')
        order.amount_paid = cash + bank
        order.balance = int(cart.summary()) - int(order.amount_paid)
        print(order.balance)
        order.save()
        for item in cart:
            try:
                remain_item = RequestOrder.objects.filter(item=item.product)
                for i in remain_item:
                    if i.remaining_quantity <= int(item.quantity):
                        i.remaining_quantity = 0
                        i.save()
                    else:
                        i.remaining_quantity = int(i.remaining_quantity) - int(item.quantity)
                        i.save()

            except Exception as e:
                messages.error(request, e)

            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.unit_price,
                quantity=item.quantity,
                attained_by=Account.objects.get(user=request.user),
            )
            cart.clear()

        messages.success(request, 'Sale Completed >- Print Receipt')
        return redirect('/sale/')
    context = {
        'form': OrderSaveForm,
        'items': Item.objects.all(),
        'cart': Cart(request),
        'quantity': QuantityForm()
    }
    return render(request, 'new_sale.html', context=context)


@login_required
def add_item_to_cart(request, key):
    """
    :param request:
    :param key:
    :return request.post -> request, new_sale.html, context{form, items ,cart, quantity}:
    :return request.get -> request, new_sale.html, context{form, items, cart, quantity}:
    """
    item = Item.objects.get(id=key)
    cart = Cart(request)
    quantityform = QuantityForm(request.POST or None)
    if quantityform.is_valid():
        # Valid form
        unit = quantityform.cleaned_data.get('unit')
        if unit <= item.get_remaining_quantity():
            # Put unit not to inventory level
            cart.update(quantity=unit, product=item, unit_price=item.price)
        else:
            cart.update(quantity=item.get_remaining_quantity(), product=item, unit_price=item.price)
            messages.error(request, '{} remaining is {}'.format(item.name, item.get_remaining_quantity()))
        return redirect('/sale/new/')
    if item.get_remaining_quantity() == 0:
        messages.error(request, 'There no {} remaining.'.format(item.name))
    else:
        cart.add(item, item.price, quantity=1)

    return redirect('/sale/new/')


@login_required
def decrease_quantity(request, key, quantity):
    item = Item.objects.get(id=key)
    cart = Cart(request)
    qty = int(quantity) - 1
    cart.update(quantity=qty, product=item, unit_price=item.price)
    return redirect('/sale/new/')


@login_required
def increase_quantity(request, key, quantity):
    item = Item.objects.get(id=key)
    cart = Cart(request)
    qty = int(quantity) - 1
    cart.update(quantity=qty, product=item, unit_price=item.price)
    return redirect('/sale/new/')


@login_required
def add_to_cart(request, product_id, quantity):
    item = Item.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(item, item.price, quantity)


@login_required
def remove_from_cart(request, key):
    product = Item.objects.get(id=key)
    cart = Cart(request)
    cart.remove(product)
    return redirect('/sale/new/')


@login_required
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return new_sale(request)


@login_required
def sale_completed(request):
    pass


@login_required
def remove_item(request, key):
    item = Item.objects.get(id=key)
    cart = Cart(request)
    cart.remove(item)
    context = {
        'form': OrderSaveForm,
        'items': Item.objects.all(),
        'cart': Cart(request),
        'quantity': QuantityForm()
    }
    return render(request, 'new_sale.html', context)


@login_required
def debtors(request):
    context = {
        'debtors': Order.objects.filter(balance__gt=0)
    }
    return render(request, 'debtors.html', context)


@login_required
def debtors_info(request, key):
    debtor = Order.objects.get(id=key)
    form = DebtForm(request.POST or None)
    if form.is_valid():
        balance = debtor.balance
        debtor.balance = int(balance) - int(form.cleaned_data.get('balance'))
        debtor.save()
        return redirect('/sale/debtors/')
    context = {
        'form': form,
        'debtor': debtor
    }
    return render(request, 'pay.html', context)
