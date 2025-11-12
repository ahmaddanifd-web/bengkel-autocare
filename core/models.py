from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()


class TimeStampedModel(models.Model):
    """Abstract model dengan timestamp"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Layanan(TimeStampedModel):
    JENIS_LAYANAN = [
        ('service_berkala', 'Service Berkala'),
        ('perbaikan_mesin', 'Perbaikan Mesin'),
        ('body_repair', 'Body Repair'),
        ('ganti_ban', 'Ganti Ban & Velg'),
        ('ac_service', 'AC Service'),
        ('electrical', 'Electrical Repair'),
    ]

    nama = models.CharField(max_length=100)
    jenis = models.CharField(max_length=30, choices=JENIS_LAYANAN)
    deskripsi = models.TextField(blank=True)
    harga_dasar = models.DecimalField(max_digits=10, decimal_places=2)
    durasi_estimasi = models.IntegerField(help_text="Durasi dalam menit")
    gambar = models.ImageField(upload_to='layanan/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['nama']
        verbose_name = "Layanan Perbaikan"
        verbose_name_plural = "Layanan Perbaikan"
        indexes = [
            models.Index(fields=['jenis']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.nama


class Mekanik(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    spesialisasi = models.CharField(max_length=100, blank=True)
    pengalaman = models.IntegerField(help_text="Pengalaman dalam tahun", default=0)
    foto = models.ImageField(upload_to='mekanik/', null=True, blank=True)
    tersedia = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['nama_lengkap']
        verbose_name = "Mekanik"
        verbose_name_plural = "Mekanik"

    def __str__(self):
        return self.nama_lengkap


class Kendaraan(TimeStampedModel):
    JENIS_KENDARAAN = [
        ('mobil', 'Mobil'),
        ('motor', 'Motor'),
    ]

    pemilik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kendaraan')
    merk = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tahun = models.IntegerField(null=True, blank=True)
    nomor_plat = models.CharField(max_length=15, unique=True)
    jenis = models.CharField(max_length=10, choices=JENIS_KENDARAAN)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kendaraan"
        verbose_name_plural = "Kendaraan"
        indexes = [
            models.Index(fields=['pemilik']),
            models.Index(fields=['nomor_plat']),
        ]

    def __str__(self):
        return f"{self.merk} {self.model} ({self.nomor_plat})"
