from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    # Booking form dan proses
    path('', views.booking_form, name='booking_form'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('list/', views.booking_list, name='booking_list'),
    path('detail/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    
    # API endpoints
    path('api/jadwal/', views.get_jadwal_tersedia, name='get_jadwal_tersedia'),
]
