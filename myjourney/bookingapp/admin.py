from django.contrib import admin
from bookingapp.models import Tourist,Pack_details,Booking,Thankyou
# Register your models here.

# admin.site.register(Tourist)
# admin.site.register(Pack_details)
# admin.site.register(Booking)
# admin.site.register(Thankyou)

class ToursitAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','mobile','email')

admin.site.register(Tourist,ToursitAdmin)

@admin.register(Pack_details)
class Pack_detailsAdmin(admin.ModelAdmin):
    list_display = ('pack_name','pack_type','pack_price')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name','pack_name','from_date','user_email','phone','adhaar_number')
    list_filter = ('from_date','pack_name')


@admin.register(Thankyou)
class ThankyouAdmin(admin.ModelAdmin):
    list_display = ('enquiry','satisfied')
    list_filter = ('satisfied',)
