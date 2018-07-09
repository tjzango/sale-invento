# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


STATUS = (('Married', 'Married'),
          ('Single', 'Single'))

LEVEL = (
    ('1', 'Administrator'),
    ('2', 'Cashier'),
    ('3', 'Store Keeper')
)


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    status = models.CharField(choices=STATUS, max_length=20)
    salary = models.PositiveIntegerField()
    joined_on = models.DateField()
    level = models.PositiveIntegerField()

    def __str__(self):
        return self.name
