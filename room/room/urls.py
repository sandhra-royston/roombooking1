from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('bookingapi/',views.BookingAPI.as_view()),
    path('bookingapi/<int:pk>',views.BookingAPI.as_view()),
]
