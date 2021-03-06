# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-01 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0009_auto_20180201_1137'),
        ('codenerix_invoicing', '0011_reasonmodificationlinealbaran_reasonmodificationlinebasket_reasonmodificationlineinvoice_reasonmodif'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleslines',
            name='tax_basket_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales_basket', to='codenerix_products.TypeTax', verbose_name='Tax Basket'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saleslines',
            name='tax_invoice_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales_invoice', to='codenerix_products.TypeTax', verbose_name='Tax Invoice'),
        ),
        migrations.AddField(
            model_name='saleslines',
            name='tax_order_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales_order', to='codenerix_products.TypeTax', verbose_name='Tax Sales order'),
        ),
        migrations.AddField(
            model_name='saleslines',
            name='tax_ticket_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales_ticket', to='codenerix_products.TypeTax', verbose_name='Tax Ticket'),
        ),
    ]
