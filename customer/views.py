# -*- coding: utf-8 -*-
# This is the file resposble for controlling all the logical operation of the customer application
# importing from python library
from __future__ import unicode_literals

# Importing from django package
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Importing forms amd database model
from customer.models import Customer
from customer.forms import AddCustomerForm
from sale.models import OrderItem


# Create your views here.
# The view all customers view
@login_required
def customer(request):
    """
    Making a query of all customers
     saving the return value to the context directive customers context
    Context can later be used in customer.html
    :param request:
    :return html file to be loaded and the context:
    """
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, 'customer.html', context)


@login_required
def customer_add(request):
    """
    This view is responsible for presenting form to an admin or cashier
    which there can use to add new customer
    :param request:
    :return:
    """
    form = AddCustomerForm(request.POST, None)
    if form.is_valid():
        # Validating form
        form.save()
        messages.success(request, "Added Customer")
        return redirect('customer:index')
    context = {
        'form': form,
    }
    return render(request, 'customer_add.html', context)


def statement(request, key):
    customer_transaction = OrderItem.objects.filter(order__customer_id=key)
    context = {
        'customer': customer_transaction
    }
    return render(request, 'statement.html', context)

"""
def customer_detail(request, key):
    goods = RequestOrder.objects.filter(supplier__id=key)
    context = {
        'goods': goods
    }
    return render(request, 'supplier_detail.html', context)
"""