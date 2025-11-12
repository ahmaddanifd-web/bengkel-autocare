from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from booking.models import Booking
from .models import Transaksi
from datetime import timedelta
from django.utils import timezone
import json

try:
    import midtransclient
except ImportError:
    midtransclient = None


@login_required
@require_http_methods(["GET"])
def payment_checkout(request, booking_id):
    """Halaman checkout pembayaran"""
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user
    )
    
    # Cek apakah transaksi sudah ada
    try:
        transaksi = Transaksi.objects.get(booking=booking)
        if transaksi.status in ['paid', 'pending']:
            if midtransclient:
                return create_payment_midtrans(request, booking, transaksi)
            else:
                return render(request, 'payment_page.html', {
                    'booking': booking,
                    'transaksi': transaksi,
                })
    except Transaksi.DoesNotExist:
        # Buat transaksi baru
        total_biaya = booking.layanan.harga_dasar
        transaksi = Transaksi.objects.create(
            booking=booking,
            total_biaya=total_biaya,
            metode_pembayaran='transfer',
            waktu_kadaluarsa=timezone.now() + timedelta(hours=24),
        )
    
    context = {
        'booking': booking,
        'transaksi': transaksi,
    }
    
    return render(request, 'payment_page.html', context)


def create_payment_midtrans(request, booking, transaksi):
    """Buat pembayaran menggunakan Midtrans"""
    try:
        snap = midtransclient.Snap(
            is_production=getattr(settings, 'MIDTRANS_IS_PRODUCTION', False),
            server_key=getattr(settings, 'MIDTRANS_SERVER_KEY', ''),
            client_key=getattr(settings, 'MIDTRANS_CLIENT_KEY', '')
        )

        param = {
            "transaction_details": {
                "order_id": f"ORDER-{booking.id}-{timezone.now().strftime('%Y%m%d%H%M%S')}",
                "gross_amount": int(booking.layanan.harga_dasar)
            },
            "customer_details": {
                "first_name": request.user.first_name or "Customer",
                "last_name": request.user.last_name or "",
                "email": request.user.email or "customer@example.com",
                "phone": getattr(request.user, 'phone', ''),
            }
        }

        transaction = snap.create_transaction(param)
        transaction_token = transaction.get('token')
        transaksi.midtrans_token = transaction_token
        transaksi.save()

        return render(request, 'payment_page.html', {
            'booking': booking,
            'transaksi': transaksi,
            'transaction_token': transaction_token,
            'client_key': getattr(settings, 'MIDTRANS_CLIENT_KEY', '')
        })
    except Exception as e:
        messages.error(request, f"Gagal membuat transaksi: {str(e)}")
        return redirect('booking:booking_detail', booking_id=booking.id)


@login_required
@require_http_methods(["GET"])
def payment_success(request):
    """Halaman sukses pembayaran"""
    booking_id = request.GET.get('booking_id')
    
    if booking_id:
        booking = get_object_or_404(
            Booking,
            id=booking_id,
            customer=request.user
        )
        transaksi = get_object_or_404(Transaksi, booking=booking)
        
        context = {
            'booking': booking,
            'transaksi': transaksi,
        }
        return render(request, 'payment_success.html', context)
    
    return redirect('core:home')


@login_required
@require_http_methods(["GET"])
def payment_failed(request):
    """Halaman gagal pembayaran"""
    booking_id = request.GET.get('booking_id')
    
    if booking_id:
        booking = get_object_or_404(
            Booking,
            id=booking_id,
            customer=request.user
        )
        transaksi = get_object_or_404(Transaksi, booking=booking)
        
        context = {
            'booking': booking,
            'transaksi': transaksi,
        }
        return render(request, 'payment_failed.html', context)
    
    return redirect('core:home')


@login_required
@require_http_methods(["GET"])
def payment_history(request):
    """Riwayat pembayaran user"""
    transaksi_list = Transaksi.objects.filter(
        booking__customer=request.user,
        is_active=True
    ).select_related('booking').order_by('-created_at')
    
    context = {'transaksi_list': transaksi_list}
    return render(request, 'payment_history.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def payment_webhook(request):
    """Webhook untuk menerima notifikasi dari payment gateway"""
    try:
        data = json.loads(request.body)
        
        # Implementasi sesuai dengan payment gateway yang digunakan
        # Contoh: Midtrans, Xendit, Stripe, dll
        
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
