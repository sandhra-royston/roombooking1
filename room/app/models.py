from django.db import models
import django.utils.timezone

# Create your models here.
class Room(models.Model):
    room_no=models.IntegerField(null=True)
    def __str__(self):
        return str(self.room_no)

class Booking(models.Model):
    name = models.CharField(max_length=50, null=True)
    room_no = models.ForeignKey(Room, null=True,
                                 on_delete=models.CASCADE,blank=True)
    checkin = models.TimeField(default=django.utils.timezone.now)
    checkout = models.TimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name





