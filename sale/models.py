# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
# Sale models defination
from django.db import models

from customer.models import Customer
from index.models import Account
from store.models import Item
from store.models import RequestOrder


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    created = models.DateTimeField(auto_now_add=True)
    cash_paid = models.IntegerField(default=0)
    bank_paid = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    attained_by = models.ForeignKey(Account)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class DebtPayment(models.Model):
    order = models.ForeignKey(Order, related_name='debt')
    balance = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Item, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    with_some = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def get_sale_cost(self):
        return self.order.amount_paid * self.quantity


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
