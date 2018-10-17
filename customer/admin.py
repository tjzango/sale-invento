# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cart.models import Item, Cart
from django.contrib import admin

from customer import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(Item)
admin.site.register(Cart)
