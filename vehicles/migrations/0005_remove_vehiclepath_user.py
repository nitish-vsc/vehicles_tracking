# Generated by Django 4.0.4 on 2022-06-28 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_vehiclepath_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclepath',
            name='user',
        ),
    ]
