from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import BookingForm, CheckingForm
from .models import Booking, Room
from .serializers import BookingSerializer

# Create your views here.


class NewBookingView(FormView):
    template_name = 'app/booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def Checking(request):
    if request.method == 'POST':
        form = CheckingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['checkin']
            check_out = form.cleaned_data['checkout']
            list = Room.objects.exclude(
                room_no__in=Room.objects.filter(bookings__checkin__lte=check_out, bookings__checkout__gte=check_in)
            ).values_list(
                'room_no', flat=True
            )
            # list = Booking.objects.filter(checkin__lte=check_out,checkout__gte=check_in).values_list('room', flat=True)
            # roomlist = Room.objects.exclude(room_no__in=list).values_list('room_no', flat=True)
        return render(request, "app/checking.html", {'form': form, 'list': list})
    form = CheckingForm()
    return render(request, "app/checking.html", {'form': form})


# class RoomList(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = BookingSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields =['bookings__checkin','bookings__checkout']
#     def get_queryset(self):
#         check_in = self.request.query_params.get('bookings__checkin')
#         check_out = self.request.query_params.get('bookings__checkout')
#         queryset = Room.objects.exclude(room_no__in=Room.objects.filter(bookings__checkin__lte=check_out,bookings__checkout__gte=check_in))
#         return queryset


class RoomFilter(filters.FilterSet):
    bookings_checkout = filters.DateTimeFilter(field_name="bookings__checkin", lookup_expr='lte')
    bookings_checkin = filters.DateTimeFilter(field_name="bookings__checkout", lookup_expr='gte')

    class Meta:
        model = Room
        fields = []


class RoomList(ListAPIView):
    queryset = Room.objects.all()
    # queryset = Room.objects.exclude(room_no__in=Room.objects.filter(bookings__checkin__lte=check_out,bookings__checkout__gte=check_in))
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields =['bookings__checkin','bookings__checkout']
    filterset_class = RoomFilter


RESPONSE_MSG = "msg"

class BookingAPI(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            room = Booking.objects.get(id=id)
            serializer = BookingSerializer(room)
            return Response(serializer.data)
        room = Booking.objects.all()
        serializer = BookingSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({RESPONSE_MSG: 'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        room = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({RESPONSE_MSG: 'Data Updated'})
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        room = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({RESPONSE_MSG: 'Data Partially Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        room = Booking.objects.get(pk=pk)
        room.delete
        return Response({RESPONSE_MSG: 'Data Deleted'})
