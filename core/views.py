from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from .models import Layanan


def home(request):
    layanan = Layanan.objects.all()[:6]
    return render(request, 'home.html', {'layanan': layanan})


@require_http_methods(["GET", "POST"])
def custom_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
