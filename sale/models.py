# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from store.models import RequestOrder
from customer.models import Customer


# Create your models here.
# Sale models defination
from django.db import models
from store.models import RequestOrder


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    created = models.DateTimeField(auto_now_add=True)
    amount_paid = models.IntegerField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(RequestOrder, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
