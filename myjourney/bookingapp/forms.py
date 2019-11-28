from django import forms
from .models import Tourist, Booking, Thankyou
from django.forms import ModelForm

class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields =[
            'first_name',
            'last_name',
            'mobile',
            'email',
            'address'
        ]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'full_name',
            'pack_name',
            'from_date',
            'user_email',
            'phone',
            'adhaar_number'
        ]
class ThankyouForm(forms.ModelForm):
    class Meta:
        model = Thankyou
        fields = [
            'enquiry',
            'satisfied'
        ]
