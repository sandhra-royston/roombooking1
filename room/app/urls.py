from django.urls import path

from .views import BookingAPI, Checking, NewBookingView, RoomList

urlpatterns = [
    
    path('roomchecking/', Checking),
    path('room/', BookingAPI.as_view()), 
    path('roomlist/', RoomList.as_view()),
    path('', NewBookingView.as_view(), name="home"),


]