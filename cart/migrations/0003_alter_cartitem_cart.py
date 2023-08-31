# Generated by Django 4.1.4 on 2023-07-06 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cart'),
        ),
    ]
