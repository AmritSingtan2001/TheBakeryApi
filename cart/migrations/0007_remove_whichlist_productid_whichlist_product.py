# Generated by Django 4.1.4 on 2023-07-26 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_product_isinstock'),
        ('cart', '0006_whichlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whichlist',
            name='productId',
        ),
        migrations.AddField(
            model_name='whichlist',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='productId', to='product.product'),
            preserve_default=False,
        ),
    ]
