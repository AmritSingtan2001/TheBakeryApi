# Generated by Django 4.2.3 on 2023-08-14 09:47

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_flavorcategorie_flavor'),
        ('orders', '0007_orderitem_is_eggless_orderitem_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='flavorcategorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='flavorCategorie', to='product.flavorcategorie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='flavorgroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.expressions.Case, related_name='flavor', to='product.flavorgroup'),
            preserve_default=False,
        ),
    ]
