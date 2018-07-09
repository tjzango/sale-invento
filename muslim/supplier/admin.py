# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from supplier import models
from store import models


# Register your models here.
admin.site.register(models.Supplier)
admin.site.register(models.RequestOrder)