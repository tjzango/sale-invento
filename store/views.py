# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib import messages

from store.models import (
    Item,
    Stock
)
from store.forms import AddItemForm
from index.models import Account


# Create your views here.
@login_required
def store(request):
    context = {
        'store': Item.objects.all()
    }
    return render(request, 'store.html', context)


def item(request, value):
    item = get_object_or_404(Item, id=value)

    context = {
        'stock': Stock.objects.filter(item=item)
    }
    return render(request, 'item.html', context)


@login_required
def add_item(request):
    form = AddItemForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            return redirect('store:index')
        except Exception as e:
            messages.error(request, e)
            print(e)

    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)
