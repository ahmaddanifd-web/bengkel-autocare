from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Booking, JadwalMekanik
from .forms import BookingForm
from core.models import Layanan, Mekanik, Kendaraan
from datetime import datetime
from django.utils import timezone


@require_http_methods(["GET"])
def get_jadwal_tersedia(request):
    """API endpoint untuk mendapatkan jadwal mekanik yang tersedia"""
    tanggal = request.GET.get('tanggal')
    layanan_id = request.GET.get('layanan_id')

    if tanggal and layanan_id:
        try:
            jadwal_tersedia = JadwalMekanik.objects.filter(
                tanggal=tanggal,
                tersedia=True,
                is_active=True
            ).values('id', 'mekanik__nama_lengkap', 'jam_mulai', 'jam_selesai')

            return JsonResponse(list(jadwal_tersedia), safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse([], safe=False)


@login_required
@require_http_methods(["GET", "POST"])
def booking_form(request):
    """Form untuk membuat booking layanan"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            
            messages.success(request, f"Booking berhasil dibuat! No. Booking: {booking.id}")
            return redirect('booking_success', booking_id=booking.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = BookingForm()

    # Filter kendaraan milik user
    kendaraan_user = Kendaraan.objects.filter(
        pemilik=request.user,
        is_active=True
    )
    
    layanan_list = Layanan.objects.filter(is_active=True).order_by('nama')

    context = {
        'form': form,
        'layanan_list': layanan_list,
        'kendaraan_user': kendaraan_user,
    }
    
    return render(request, 'booking_form.html', context)


@login_required
@require_http_methods(["GET"])
def booking_success(request, booking_id):
    """Halaman sukses setelah booking berhasil dibuat"""
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user
    )
    
    context = {'booking': booking}
    return render(request, 'booking_success.html', context)


@login_required
@require_http_methods(["GET"])
def booking_list(request):
    """Daftar booking milik user"""
    bookings = Booking.objects.filter(
        customer=request.user,
        is_active=True
    ).select_related('kendaraan', 'layanan', 'mekanik').order_by('-created_at')
    
    context = {'bookings': bookings}
    return render(request, 'booking_list.html', context)


@login_required
@require_http_methods(["GET"])
def booking_detail(request, booking_id):
    """Detail booking tertentu"""
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user
    )
    
    context = {'booking': booking}
    return render(request, 'booking_detail.html', context)
