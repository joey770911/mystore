# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='產品名稱')),
                ('description', models.TextField(verbose_name='產品敘述')),
                ('quantity', models.IntegerField(verbose_name='庫存數量')),
                ('price', models.IntegerField(verbose_name='價格')),
            ],
        ),
    ]
