# Generated by Django 4.2.2 on 2023-06-20 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_room_no_booking_room_booking_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
