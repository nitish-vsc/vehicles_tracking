# Generated by Django 4.0.4 on 2022-06-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathdetail',
            name='arrival_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pathdetail',
            name='depature_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]