from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Layanan(models.Model):
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

    def __str__(self):
        return self.nama


class Mekanik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    spesialisasi = models.CharField(max_length=100, blank=True)
    pengalaman = models.IntegerField(help_text="Pengalaman dalam tahun", default=0)
    foto = models.ImageField(upload_to='mekanik/', null=True, blank=True)
    tersedia = models.BooleanField(default=True)

    def __str__(self):
        return self.nama_lengkap


class Kendaraan(models.Model):
    JENIS_KENDARAAN = [
        ('mobil', 'Mobil'),
        ('motor', 'Motor'),
    ]

    pemilik = models.ForeignKey(User, on_delete=models.CASCADE)
    merk = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tahun = models.IntegerField(null=True, blank=True)
    nomor_plat = models.CharField(max_length=15)
    jenis = models.CharField(max_length=10, choices=JENIS_KENDARAAN)

    def __str__(self):
        return f"{self.merk} {self.model} ({self.nomor_plat})"
