
from django.contrib import admin
from .models import Booking,Room
# Register your models here.

admin.site.register(Room)
# admin.site.register(Booking)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','room','checkin','checkout']