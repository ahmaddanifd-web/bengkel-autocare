from django.db import models
from booking.models import Booking
import random
import string


class Transaksi(models.Model):
    STATUS_PEMBAYARAN = [
        ('pending', 'Menunggu Pembayaran'),
        ('paid', 'Terbayar'),
        ('failed', 'Gagal'),
        ('expired', 'Kadaluarsa'),
    ]

    METODE_PEMBAYARAN = [
        ('transfer', 'Transfer Bank'),
        ('ewallet', 'E-Wallet'),
        ('qris', 'QRIS'),
        ('tunai', 'Tunai'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    kode_transaksi = models.CharField(max_length=20, unique=True, blank=True)
    total_biaya = models.DecimalField(max_digits=12, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=20, choices=METODE_PEMBAYARAN)
    status = models.CharField(max_length=20, choices=STATUS_PEMBAYARAN, default='pending')
    waktu_transaksi = models.DateTimeField(auto_now_add=True)
    waktu_kadaluarsa = models.DateTimeField()
    midtrans_token = models.CharField(max_length=255, blank=True)

    def generate_kode_transaksi(self):
        return f"TRX{self.booking.id:06d}{''.join(random.choices(string.digits, k=4))}"

    def save(self, *args, **kwargs):
        if not self.kode_transaksi:
            self.kode_transaksi = self.generate_kode_transaksi()
        super().save(*args, **kwargs)
