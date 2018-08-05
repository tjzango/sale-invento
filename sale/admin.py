# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from sale import models


# Register your models here.
admin.site.register(models.Order)
admin.site.register(models.OrderItem)