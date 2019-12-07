# Generated by Django 2.2.7 on 2019-12-06 05:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0003_auto_20191206_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_num',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^[0]\\d{9,10}$')]),
        ),
    ]
