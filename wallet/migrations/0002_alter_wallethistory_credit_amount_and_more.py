# Generated by Django 4.0.4 on 2022-06-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallethistory',
            name='credit_amount',
            field=models.FloatField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='wallethistory',
            name='debit_amount',
            field=models.FloatField(blank=True, max_length=50),
        ),
    ]
