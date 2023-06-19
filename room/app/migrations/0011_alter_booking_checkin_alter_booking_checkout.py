# Generated by Django 4.2.2 on 2023-06-15 23:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_booking_checkin_alter_booking_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]