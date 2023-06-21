from django.forms import ModelForm, forms
from django.db.models import Q
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('checkin')
        check_out = cleaned_data.get('checkout')
        room = cleaned_data.get('room')
        if check_in > check_out:
            raise forms.ValidationError('checkout date should be after checkindate')
        bookingList = Booking.objects.filter(checkin__lte=check_out,checkout__gte=check_in,room=room)
        if bookingList:
            raise forms.ValidationError('This Room is already booked for the selected datetime slot,select another')


        # if Booking.objects.filter(room_no=room_no).exists():
        #     bookingList = Booking.objects.filter(room_no=room_no)
        #     for instance in bookingList:
        #         if ((instance.checkin <= checkout) and (instance.checkout >= checkin)) :
        #             raise forms.ValidationError('This Room is already booked select another')