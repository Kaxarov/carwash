# Generated by Django 3.2.6 on 2022-02-16 05:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True, validators=[django.core.validators.RegexValidator('[A-Za-z0-9]{5,}')], verbose_name='Username'),
        ),
    ]
