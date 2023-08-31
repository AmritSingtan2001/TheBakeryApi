# Generated by Django 4.1.4 on 2023-05-29 05:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_product_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]