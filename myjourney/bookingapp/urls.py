from django.urls import path
from bookingapp.views import tourist_view, booking_view, pack_details_view,thankyou_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tourist/', views.tourist_view, name='tourist'),
    # path('pack_details/', views.pack_details_view, name='pack_details'),
    path('booking/', views.booking_view, name='booking'),
    path('pack_details/', views.pack_details_view, name='pack_details'),
    path('thankyou/', views.thankyou_view, name='thankyou'),



]
