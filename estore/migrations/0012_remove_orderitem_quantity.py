# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 05:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0011_cart_items_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
