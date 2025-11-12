from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    # Payment gateway URLs
    path('checkout/<int:booking_id>/', views.payment_checkout, name='payment_checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('failed/', views.payment_failed, name='payment_failed'),
    path('history/', views.payment_history, name='payment_history'),
    
    # Webhook untuk payment gateway
    path('webhook/', views.payment_webhook, name='payment_webhook'),
]
