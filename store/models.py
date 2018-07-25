# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from index.models import Account
from supplier.models import Supplier

ACTIONS = (
    ('receive', 'receive'),
    ('return', 'return')
)


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_chech_url(self):
        return reverse('store:item', args=[self.id])

    def get_remaining_quantity(self):
        return sum(item.quantity for item in self.items.all())


class RequestOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    bill_no = models.CharField(max_length=20)
    requested_quantity = models.PositiveIntegerField()
    received_quantity = models.PositiveIntegerField(default=0)
    requested_price = models.PositiveIntegerField()
    received_price = models.PositiveIntegerField(default=0)
    stocked = models.BooleanField(default=False)
    action = models.CharField(choices=ACTIONS, max_length=20)

    def __str__(self):
        return '{}, {}'.format(self.item, self.supplier)


class Stock(models.Model):
    item = models.ForeignKey(Item, related_name='items')
    quantity = models.PositiveIntegerField(default=0)
    added_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    order = models.ForeignKey(RequestOrder, on_delete=models.CASCADE)
    remaining = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.item)
