from django.urls import path
from .views import NewBookingView


urlpatterns = [
    path('', NewBookingView.as_view(), name="home"),

]