# Generated by Django 4.1.4 on 2023-07-26 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_coupon_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhome',
            old_name='alternativeNo',
            new_name='altPhoneNo',
        ),
        migrations.RenameField(
            model_name='userhome',
            old_name='districts',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='userhome',
            old_name='fullname',
            new_name='fullName',
        ),
        migrations.RenameField(
            model_name='userhome',
            old_name='landmark',
            new_name='landMark',
        ),
        migrations.RenameField(
            model_name='userhome',
            old_name='phoneNumber',
            new_name='phoneNo',
        ),
    ]