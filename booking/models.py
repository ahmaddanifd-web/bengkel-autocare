from django.db import models
from django.conf import settings
from core.models import Layanan, Mekanik, Kendaraan


class Booking(models.Model):
    STATUS_BOOKING = [
        ('menunggu', 'Menunggu Konfirmasi'),
        ('dikonfirmasi', 'Dikonfirmasi'),
        ('diproses', 'Sedang Diproses'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE)
    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE)
    mekanik = models.ForeignKey(Mekanik, on_delete=models.SET_NULL, null=True, blank=True)
    tanggal_booking = models.DateTimeField()
    keluhan = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_BOOKING, default='menunggu')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking #{self.id} - {self.customer}"


class JadwalMekanik(models.Model):
    mekanik = models.ForeignKey(Mekanik, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    tersedia = models.BooleanField(default=True)

    class Meta:
        unique_together = ['mekanik', 'tanggal', 'jam_mulai']

    def __str__(self):
        return f"{self.mekanik.nama_lengkap} - {self.tanggal} {self.jam_mulai}"
