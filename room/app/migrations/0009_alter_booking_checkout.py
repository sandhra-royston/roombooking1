# Generated by Django 4.2.2 on 2023-06-15 00:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_booking_time_booking_checkin_booking_checkout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
