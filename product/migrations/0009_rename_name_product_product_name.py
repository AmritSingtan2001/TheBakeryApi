# Generated by Django 4.1.4 on 2023-05-26 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_isinstock_product_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
