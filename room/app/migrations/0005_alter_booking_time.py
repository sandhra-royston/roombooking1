# Generated by Django 4.2.2 on 2023-06-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
