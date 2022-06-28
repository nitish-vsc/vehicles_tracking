# Generated by Django 4.0.4 on 2022-06-28 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('vehicles', '0005_remove_vehiclepath_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclepath',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.registeruser'),
            preserve_default=False,
        ),
    ]
