# Generated by Django 2.2.7 on 2019-12-10 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consistof',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
