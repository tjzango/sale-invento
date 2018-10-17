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
# Item defination models defination
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_chech_url(self):
        return reverse('store:item', args=[self.id])

    def get_remaining_quantity(self):
        return sum(item.remaining_quantity for item in self.items.all())


# Request order defination
class RequestOrder(models.Model):
    item = models.ForeignKey(Item, related_name='items')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    bill_no = models.CharField(max_length=20)
    requested_quantity = models.PositiveIntegerField()
    received_quantity = models.PositiveIntegerField(default=0)
    requested_price = models.PositiveIntegerField()
    received_price = models.PositiveIntegerField(default=0)
    stocked = models.BooleanField(default=False)
    action = models.CharField(choices=ACTIONS, max_length=20)
    remaining_quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.item, self.supplier)

    class Meta:
        ordering = ['remaining_quantity']


