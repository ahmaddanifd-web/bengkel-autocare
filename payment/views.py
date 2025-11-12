import midtransclient
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Transaksi
from booking.models import Booking


@login_required
def create_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    snap = midtransclient.Snap(
        is_production=False,
        server_key=settings.MIDTRANS_SERVER_KEY,
        client_key=settings.MIDTRANS_CLIENT_KEY
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
            "phone": getattr(request.user, 'phone', '089502640906'),
        }
    }

    transaction = snap.create_transaction(param)
    transaction_token = transaction.get('token')

    transaksi = Transaksi.objects.create(
        booking=booking,
        total_biaya=booking.layanan.harga_dasar,
        metode_pembayaran='transfer',
        waktu_kadaluarsa=timezone.now() + timezone.timedelta(hours=24)
    )

    return render(request, 'payment_page.html', {
        'transaction_token': transaction_token,
        'transaksi': transaksi
    })


def payment_notification(request):
    # TODO: implement Midtrans webhook handling
    return render(request, 'payment_notification.html', {})
