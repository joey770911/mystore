# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estore', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_name', models.CharField(max_length=255, verbose_name='購買人姓名')),
                ('billing_address', models.CharField(max_length=255, verbose_name='購買人地址')),
                ('shipping_name', models.CharField(max_length=255, verbose_name='收件人姓名')),
                ('shipping_address', models.CharField(max_length=255, verbose_name='收件人地址')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='產品名稱')),
                ('price', models.IntegerField(verbose_name='價格')),
                ('quantity', models.IntegerField(verbose_name='數量')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='estore.OrderInfo', verbose_name='訂購資訊')),
                ('total', models.IntegerField(default=0, verbose_name='總價')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='訂購使用者')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estore.Order'),
        ),
    ]
