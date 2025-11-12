from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Booking, JadwalMekanik
from core.models import Layanan, Mekanik, Kendaraan
from datetime import datetime
from django.utils import timezone


def get_jadwal_tersedia(request):
    tanggal = request.GET.get('tanggal')
    layanan_id = request.GET.get('layanan_id')

    if tanggal and layanan_id:
        jadwal_tersedia = JadwalMekanik.objects.filter(
            tanggal=tanggal,
            tersedia=True
        ).values('jam_mulai', 'jam_selesai')

        return JsonResponse(list(jadwal_tersedia), safe=False)

    return JsonResponse([], safe=False)


@login_required
def booking_form(request):
    if request.method == 'POST':
        kendaraan_id = request.POST.get('kendaraan')
        layanan_id = request.POST.get('layanan')
        tanggal = request.POST.get('tanggal')
        jam = request.POST.get('jam')
        keluhan = request.POST.get('keluhan')

        kendaraan = get_object_or_404(Kendaraan, id=kendaraan_id, pemilik=request.user)
        layanan = get_object_or_404(Layanan, id=layanan_id)

        mekanik_tersedia = Mekanik.objects.filter(
            tersedia=True,
            jadwalmekanik__tanggal=tanggal,
            jadwalmekanik__jam_mulai=jam,
            jadwalmekanik__tersedia=True
        ).first()

        booking = Booking.objects.create(
            customer=request.user,
            kendaraan=kendaraan,
            layanan=layanan,
            mekanik=mekanik_tersedia,
            tanggal_booking=datetime.strptime(f"{tanggal} {jam}", "%Y-%m-%d %H:%M"),
            keluhan=keluhan
        )

        return render(request, 'booking_success.html', {'booking': booking})

    layanan_list = Layanan.objects.all()
    kendaraan_user = Kendaraan.objects.filter(pemilik=request.user) if request.user.is_authenticated else []

    return render(request, 'booking_form.html', {
        'layanan_list': layanan_list,
        'kendaraan_user': kendaraan_user
    })
