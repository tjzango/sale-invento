# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    get_object_or_404,
)


from supplier.models import Supplier
from supplier.forms import AddSupplierForm

from store.models import (
    RequestOrder,
    Stock
)
from store.forms import (
    RequestOrderForm,
    StockOrderForm
)
from index.models import Account


# Create your views here.
@login_required
def supplier(request):
    context = {
        'suppliers': Supplier.objects.all()
    }
    return render(request, 'supplier.html', context)


@login_required
def supplier_add(request):
    form = AddSupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Added Supplier")
        return redirect('supplier:index')
    context = {
        'form': form,
    }
    return render(request, 'supplier_add.html', context)


@login_required
def order(request):
    context = {
        'orders': RequestOrder.objects.filter(action='receive')
    }
    return render(request, 'order.html', context)


def order_request(request):
    if request.method == "POST":
        form = RequestOrderForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Account, user=request.user)
            instance = form.save(commit=False)
            instance.requested_by = user
            instance.save()
            print(instance)
            messages.success(request, "Requested {}".format(form.cleaned_data.get('item')))
            return redirect('supplier:order')

    context = {
        'form': RequestOrderForm
    }
    return render(request, 'order_request.html', context)


def order_stock(request, key):
    order = get_object_or_404(RequestOrder, id=key)
    form = StockOrderForm(request.POST or None)
    if form.is_valid():
        order.received_price = form.cleaned_data.get('received_price')
        order.received_quantity = form.cleaned_data.get('received_quantity')
        order.stocked = True
        order.save()
        messages.success(request, "Received Items --> store")
        return redirect('supplier:order')
    context = {
        'order': order,
        'form': form
    }
    return render(request, 'order_stock.html', context)


def supplier_detail(request, key):
    context = {
        'goods': RequestOrder.objects.filter(supplier__id=key)
    }
    return render(request, 'supplier_detail.html', context)
