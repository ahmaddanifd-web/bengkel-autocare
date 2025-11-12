from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_form, name='booking_form'),
    path('jadwal/', views.get_jadwal_tersedia, name='get_jadwal_tersedia'),
]
