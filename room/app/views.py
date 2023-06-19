from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def home(request):
    form=BookingForm()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"app/booking.html",context)