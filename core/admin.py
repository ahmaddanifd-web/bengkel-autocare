from django.contrib import admin
from .models import Layanan, Mekanik, Kendaraan


@admin.register(Layanan)
class LayananAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis', 'harga_dasar', 'durasi_estimasi')
    list_filter = ('jenis',)
    search_fields = ('nama', 'deskripsi')
    fieldsets = (
        ('Info Layanan', {
            'fields': ('nama', 'jenis', 'deskripsi')
        }),
        ('Harga & Durasi', {
            'fields': ('harga_dasar', 'durasi_estimasi')
        }),
        ('Media', {
            'fields': ('gambar',)
        }),
    )


@admin.register(Mekanik)
class MekanikAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'spesialisasi', 'pengalaman', 'tersedia')
    list_filter = ('tersedia', 'spesialisasi')
    search_fields = ('nama_lengkap', 'user__username')
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Info Mekanik', {
            'fields': ('nama_lengkap', 'spesialisasi', 'pengalaman')
        }),
        ('Status', {
            'fields': ('tersedia',)
        }),
        ('Media', {
            'fields': ('foto',)
        }),
    )


@admin.register(Kendaraan)
class KendaraanAdmin(admin.ModelAdmin):
    list_display = ('nomor_plat', 'merk', 'model', 'jenis', 'pemilik')
    list_filter = ('jenis', 'tahun')
    search_fields = ('nomor_plat', 'merk', 'model', 'pemilik__username')
    fieldsets = (
        ('Pemilik', {
            'fields': ('pemilik',)
        }),
        ('Info Kendaraan', {
            'fields': ('merk', 'model', 'tahun', 'jenis')
        }),
        ('Plat', {
            'fields': ('nomor_plat',)
        }),
    )
