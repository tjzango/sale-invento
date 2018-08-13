# -*- coding: utf-8 -*-
# This file contain all our model(databasse table) defination of the index application
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# STATUS AND LEVELS Are choices wewant to use in Account and Employee table
STATUS = (('Married', 'Married'),
          ('Single', 'Single'))

LEVEL = (
    ('Administrator', 'Administrator'),
    ('Cashier', 'Cashier'),
    ('Store Keeper', 'Store Keeper')
)

EMPLOYEE_LEVEL = (
    ('Manager', 'Manager'),
    ('Cleaner', 'Cleaner'),
    ('Cashier', 'Cashier'),
    ('Store Keeper', 'Store Keeper'),
    ('Other', 'Other')
)
# Create your models here.
# Users account defination e.g muslim has attribute user, contact and level
# user has a forignkey to the User(first_name, last_name, password, username and email) models
# contact is a VARCHAR Field
# level is contain either three values 1,2 or 3 i.e Administrator, cashier or storekeeper respectively
# Employee Defination


class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    status = models.CharField(choices=STATUS, max_length=20)
    salary = models.PositiveIntegerField()
    joined_on = models.DateField()
    level = models.CharField(max_length=20, choices=EMPLOYEE_LEVEL)
    contact = models.CharField(max_length=20, default='1')

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)

    def __str__(self):
        return "{} to {}".format(self.body, self.user)
