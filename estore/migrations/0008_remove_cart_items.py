# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0007_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
    ]
