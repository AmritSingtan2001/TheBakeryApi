# Generated by Django 4.1.4 on 2023-05-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_category_image1_category_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_views',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
