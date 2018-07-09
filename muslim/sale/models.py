# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from store.models import Stock
from customer.models import Customer


# Create your models here.
class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class Invoice(models.Model):
    sale = models.ForeignKey(Sale, related_name='items')
    product = models.ForeignKey(Stock,  related_name='order_items')
    invoice_no = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return "{} {}".format(self.product.item.name, self.invoice_no)

    def get_cost(self):
        return self.price * self.quantity
