# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from sale.forms import OrderSaveForm, QuantityForm
from cart.cart import Cart
from store.models import Item
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
    context = {
        'sales': OrderItem.objects.all()
    }
    return render(request, 'sale.html', context)


@login_required
def new_sale(request):
    """
    This view is responsible for allowing users making new sale
    :param request:
    :return request, new_sale.html, context{form, items}:
    """
    order_form = OrderSaveForm(request.POST or None)
    if order_form.is_valid():
        order = order_form.save()
        cart = Cart(request)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.unit_price,
                quantity=item.quantity,
                attained_by=Account.objects.get(user=request.user)
            )
        cart.clear()
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
    context = {
        'form': OrderSaveForm,
        'items': Item.objects.all(),
        'cart': Cart(request),
        'quantity': QuantityForm()
    }
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
