# Generated by Django 4.1.4 on 2023-05-26 12:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rename_name_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='product_name', unique=True),
        ),
    ]
