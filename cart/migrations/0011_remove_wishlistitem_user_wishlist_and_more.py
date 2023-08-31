# Generated by Django 4.2.3 on 2023-08-03 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0010_remove_wishlistitem_wishlist_wishlistitem_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='user',
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userWhichlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='wishlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='cart.wishlist'),
            preserve_default=False,
        ),
    ]