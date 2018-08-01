# -*- coding: utf-8 -*-
# This file contain all our model(databasse table) defination of the customer application
from __future__ import unicode_literals

from django.db import models


# Create your models here.
# Our firest models customer which has name and contact
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
