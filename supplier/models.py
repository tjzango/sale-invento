# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from index.models import User


# Create your models here.
# Ssupplier models defination
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


