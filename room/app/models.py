from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Room(models.Model):
    room_no=models.IntegerField()
    def __str__(self):
        return str(self.room_no)

class Booking(models.Model):
    name = models.CharField(max_length=50, null=True)
    room = models.ForeignKey(Room, null=True,
                                 on_delete=models.CASCADE,blank=True)
    # date=models.DateField(default=datetime.date.today,null=True)
    # checkin = models.TimeField(default=timezone.now)
    # checkout = models.TimeField(default=timezone.now)
    checkin=models.DateTimeField(default=timezone.now)
    checkout=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name





