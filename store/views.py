# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from store.forms import AddItemForm
from store.models import (
    Item,
    RequestOrder
)


# Create your views here.
@login_required
def store(request):
    """
    This view is responsible of quering all item in the store
    and lodding the store.html file which will display all items from 'store' context
    :param request:
    :return:
    """
    context = {
        'store': Item.objects.all()
    }
    return render(request, 'store.html', context)


@login_required
def item(request, value):
    """
    This view is responsible for allowing users view
    statement of a particular item in the store
    :param request:
    :param value:
    :return:
    """
    item = get_object_or_404(Item, id=value)

    context = {
        'stock': RequestOrder.objects.filter(item=item)
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
