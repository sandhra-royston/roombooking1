from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.db.models import CheckConstraint, Q, F


class Room(models.Model):
    room_no=models.IntegerField()
    def __str__(self):
        return str(self.room_no)

class Booking(models.Model):
    class Meta:
        constraints = [
            CheckConstraint(
                name='check_room_booking',
                check=Q(room_name__isnull=False) &
                Q(date__isnull=False) &
                Q(checkin__lte=F('checkout')) &
                Q(checkout__gte=F('checkin'))
                )
        ]

    name = models.CharField(max_length=50, null=True)
    room = models.ForeignKey(Room, null=True,
                                 on_delete=models.CASCADE,blank=True, related_name="bookings")
    checkin=models.DateTimeField(default=timezone.now)
    checkout=models.DateTimeField(default=timezone.now)

    def clean(self):
        super().clean()
        booked_rooms = Booking.objects.filter(
                room=self.room,
                checkin__lte=self.checkout,
                checkout__gte=self.checkin
            ).exists()
        if booked_rooms:
                raise ValidationError(("This room is already booked for this time."))
    def __str__(self):
        return self.name





