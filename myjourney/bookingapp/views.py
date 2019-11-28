from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.from django.shortcuts import render
from django.http import HttpResponse
from .forms import TouristForm, BookingForm, ThankyouForm
from .models import Tourist, Booking, Pack_details
from django.views import generic

def index(request):
    """View function for home page of site."""
    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def tourist_view(request):
    form = TouristForm(request.POST or None)
    if form.is_valid():
        form.save()


    context = {
    'form': form
    }
    return render(request,"bookingapp/tourist.html", context)

def booking_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
    'form': form
    }
    return render(request,"bookingapp/booking.html", context)

def pack_details_view(request):

    all_details= Pack_details.objects.all()

    context= {'all_details': all_details}

    return render(request, 'bookingapp/pack_details.html', context)

def thankyou_view(request):
    form = ThankyouForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
    'form': form
    }
    return render(request,"bookingapp/Thankyou.html", context)
