from django.db import models
from booking.models import Booking
from core.models import TimeStampedModel
import uuid


class Transaksi(TimeStampedModel):
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

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='transaksi')
    kode_transaksi = models.CharField(
        max_length=36, 
        unique=True, 
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )
    total_biaya = models.DecimalField(max_digits=12, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=20, choices=METODE_PEMBAYARAN)
    status = models.CharField(max_length=20, choices=STATUS_PEMBAYARAN, default='pending', db_index=True)
    waktu_kadaluarsa = models.DateTimeField()
    midtrans_token = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Transaksi"
        verbose_name_plural = "Transaksi"
        indexes = [
            models.Index(fields=['booking']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Transaksi {self.kode_transaksi} - {self.booking}"
