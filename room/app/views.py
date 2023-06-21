from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import BookingForm
from django.urls import reverse_lazy


# Create your views here.
class NewBookingView(FormView):
    template_name = 'app/booking.html'
    form_class= BookingForm
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def home(request):
#     form=BookingForm()
#     if request.method=='POST':
#         form=BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context={'form':form}
#     return render(request,"app/booking.html",context)