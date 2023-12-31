# Generated by Django 4.1.4 on 2023-05-23 07:03

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
                ('category_slug', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='category_name', unique=True)),
            ],
        ),
    ]
