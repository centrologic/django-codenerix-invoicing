# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-30 12:47
from __future__ import unicode_literals

import codenerix.fields
import codenerix.lib.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0008_auto_20180130_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrderDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('doc_path', codenerix.fields.FileAngularField(max_length=200, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Doc Path')),
                ('name_file', models.CharField(max_length=254, verbose_name='Name')),
                ('notes', models.TextField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_document_sales', to='codenerix_invoicing.TypeDocument', verbose_name='Document type')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_document_sales', to='codenerix_invoicing.SalesOrder', verbose_name='Sales order')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
            },
        ),
    ]