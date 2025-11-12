from django.shortcuts import render
from .models import Layanan


def home(request):
    layanan = Layanan.objects.all()[:6]
    return render(request, 'home.html', {'layanan': layanan})
