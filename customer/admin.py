# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from customer import models
from  cart.models import Item, ItemManager, Cart


# Register your models here.
admin.site.register(models.Customer)
admin.site.register(Item)
admin.site.register(Cart)
