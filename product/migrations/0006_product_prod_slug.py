# Generated by Django 4.1.4 on 2023-05-24 06:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='name', unique=True),
        ),
    ]
