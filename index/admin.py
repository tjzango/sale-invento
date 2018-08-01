# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Admin ad database import
from django.contrib import admin
from index import models
# Register your models here.

# Database Registration to the admin site i.e locahost:8000/admin/index/
admin.site.register(models.Account)
admin.site.register(models.Employee)