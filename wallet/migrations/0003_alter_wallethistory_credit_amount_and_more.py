# Generated by Django 4.0.4 on 2022-06-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_wallethistory_credit_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallethistory',
            name='credit_amount',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wallethistory',
            name='debit_amount',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]
