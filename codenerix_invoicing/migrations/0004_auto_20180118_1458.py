# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-18 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0003_saleslinealbaran_invoiced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseslinealbaran',
            name='validator_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='line_albaran_purchases', to=settings.AUTH_USER_MODEL, verbose_name='Validator user'),
        ),
    ]
