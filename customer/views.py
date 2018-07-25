# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from customer.models import Customer
from customer.forms import AddCustomerForm


# Create your views here.
@login_required
def customer(request):
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, 'customer.html', context)


@login_required
def customer_add(request):
    form = AddCustomerForm(request.POST, None)
    if form.is_valid():
        form.save()
        messages.success(request, "Added Customer")
        return redirect('customer:index')
    context = {
        'form': form,
    }
    return render(request, 'customer_add.html', context)
