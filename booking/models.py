from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from core.models import Layanan, Mekanik, Kendaraan, TimeStampedModel


class Booking(TimeStampedModel):
    STATUS_BOOKING = [
        ('menunggu', 'Menunggu Konfirmasi'),
        ('dikonfirmasi', 'Dikonfirmasi'),
        ('diproses', 'Sedang Diproses'),
        ('selesai', 'Selesai'),
        ('dibatalkan', 'Dibatalkan'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE, related_name='bookings_list')
    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE, related_name='bookings')
    mekanik = models.ForeignKey(Mekanik, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings_assigned')
    tanggal_booking = models.DateTimeField()
    keluhan = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_BOOKING, default='menunggu')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Booking"
        verbose_name_plural = "Booking"
        unique_together = [['kendaraan', 'mekanik', 'tanggal_booking']]
        indexes = [
            models.Index(fields=['customer', 'status']),
            models.Index(fields=['tanggal_booking']),
            models.Index(fields=['status']),
        ]

    def clean(self):
        if self.tanggal_booking <= timezone.now():
            raise ValidationError("Tanggal booking harus di masa depan")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer}"


class JadwalMekanik(TimeStampedModel):
    mekanik = models.ForeignKey(Mekanik, on_delete=models.CASCADE, related_name='jadwal')
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    tersedia = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['mekanik', 'tanggal', 'jam_mulai']
        verbose_name = "Jadwal Mekanik"
        verbose_name_plural = "Jadwal Mekanik"
        ordering = ['tanggal', 'jam_mulai']
        indexes = [
            models.Index(fields=['mekanik', 'tanggal']),
            models.Index(fields=['tersedia']),
        ]

    def __str__(self):
        return f"{self.mekanik.nama_lengkap} - {self.tanggal} {self.jam_mulai}"
