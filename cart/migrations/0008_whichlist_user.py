# Generated by Django 4.1.4 on 2023-07-27 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0007_remove_whichlist_productid_whichlist_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='whichlist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userWhichlist', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
