# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-25 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180724_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestorder',
            name='received_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
