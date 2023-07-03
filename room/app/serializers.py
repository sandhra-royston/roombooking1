from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        if data['checkin'] > data['checkout']:
            raise serializers.ValidationError(
                "checkout date must come after checkin date"
            )
        else:
            booked_rooms = Booking.objects.some()
            if booked_rooms:
                raise serializers.ValidationError(("This room is already booked for this time."))
        return data
