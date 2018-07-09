# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from index import models
# Register your models here.


admin.site.register(models.Account)
admin.site.register(models.Employee)