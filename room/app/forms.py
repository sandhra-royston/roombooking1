from django.forms import ModelForm, forms

from .models import Booking


class BookingForm(ModelForm):
    # checkin=forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model=Booking
        fields='__all__'

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')
        room_no = cleaned_data.get('room_no')
        if Booking.objects.filter(room_no=room_no).exists():
            bookingList = Booking.objects.filter(room_no=room_no)
            for instance in bookingList:
                if ((instance.checkin <= checkout) and (instance.checkout >= checkin)) :
                    raise forms.ValidationError('This Room is already booked select another')
        # else:
        #     print("0000")

            # print('instance checkin-',instance.checkin)
            # print('instance checkout-', instance.checkout)
            # print(instance.checkin>checkout)
            # print(instance.checkout < checkin)
            # print("------")
            # print(((instance.checkin >= checkout) and (instance.checkout <= checkin)))
