# Generated by Django 4.1.4 on 2023-05-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_rename_discription_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image1',
            field=models.ImageField(default=1, upload_to='cakecategoryimage/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image2',
            field=models.ImageField(default=1, upload_to='cakecategoryimage/'),
            preserve_default=False,
        ),
    ]