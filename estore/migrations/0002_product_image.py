# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='商品圖片'),
        ),
    ]
