# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    get_object_or_404
)
from django.template.loader import get_template
from django.core.urlresolvers import reverse_lazy
from index.models import Account
from sale.forms import (
    DebtForm,
    ExpenseForm,
    QuantityForm,
    OrderSaveForm,
)
from sale.models import (
    Order,
    Expense,
    OrderItem,
    DebtPayment,
)
from store.models import (
    Item,
    RequestOrder
)


# Create your views here.
@login_required
def index(request):
    """
    This view is responsible for loading the sale.html file
    :param request:
    :return:
    """
    sales = OrderItem.objects.filter(visible=True)
    order = Order.objects.filter(visible=True)
    expenses = Expense.objects.all()
    total_expenses = sum(item.amount for item in expenses)
    total_sale = sum(item.amount_paid for item in order)
    total_amount_made = total_sale - total_expenses
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
        order.amount_paid = int(cart.summary())
        order.balance = 0
        order.attained_by = Account.objects.get(user=request.user)
        order.save()

        for item in cart:
            try:
                remain_item = RequestOrder.objects.filter(item=item.product)
                for i in remain_item:

                    print(5)
                    if i.remaining_quantity <= int(item.quantity):
                        i.remaining_quantity = 0
                        i.save()
                    else:
                        print(6)
                        i.remaining_quantity = int(i.remaining_quantity) - int(item.quantity)
                        i.save()

            except Exception as e:
                messages.error(request, e)

            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.unit_price,
                quantity=item.quantity,
            )
            cart.clear()

        messages.error(request, 'Transaction with {} have been made.'.format(order.customer))
        return redirect('sale:index')

    context = {
        'form': OrderSaveForm,
        'items': Item.objects.all(),
        'cart': Cart(request),
        'quantity': QuantityForm(),

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
        'debtors': Order.objects.filter(balance__gt=0),
        'paid_debt': DebtPayment.objects.filter()
    }
    return render(request, 'debtors.html', context)


@login_required
def debtors_info(request, key):
    debtor = Order.objects.get(id=key)
    form = DebtForm(request.POST or None)
    if form.is_valid():
        balance = debtor.balance
        DebtPayment.objects.create(balance=debtor.balance, paid=int(form.cleaned_data.get('balance')), order=debtor)
        debtor.balance = int(balance) - int(form.cleaned_data.get('balance'))
        debtor.save()
        return redirect('/sale/debtors/')
    context = {
        'form': form,
        'debtor': debtor
    }
    return render(request, 'pay.html', context)


@login_required
def expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        amount = form.cleaned_data.get('amount')

        form.save()

        return redirect('/sale/expense/')
    context = {
        'form': form,
        'expenses': Expense.objects.all()
    }
    return render(request, 'expense.html', context)


@login_required
def invoice(request, key):
    template = get_template('invoice.html')
    order = get_object_or_404(Order, id=key)
    context = {
        'order': order,
        'order_item_set': get_list_or_404(OrderItem, order=order),
        'debt': DebtPayment.objects.filter(order=order)
    }
    return render(request, 'invoicee.html', context)


@login_required
def edit(request, key):
    order = get_object_or_404(Order, id=key, visible=True)
    context = {
        'order': order,
        'order_item_set': get_list_or_404(OrderItem, order=order),
    }
    return render(request, 'edit.html', context)


@login_required
def remove(request, key):
    order = get_object_or_404(Order, id=key)
    order.visible = False
    items = OrderItem.objects.filter(order=order)
    for i in items:
        i.visible = False
        i.save()

    order.save()
    context = {
        'order': order,
        'order_item_set': get_list_or_404(OrderItem, order=order),
    }
    return redirect('sale:index')
