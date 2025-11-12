from django.contrib import admin
from .models import Booking, JadwalMekanik


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'kendaraan', 'layanan', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'mekanik')
    search_fields = ('customer__username', 'kendaraan__nomor_plat', 'keluhan')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Info Booking', {
            'fields': ('customer', 'kendaraan', 'layanan', 'mekanik')
        }),
        ('Tanggal & Keluhan', {
            'fields': ('tanggal_booking', 'keluhan')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(JadwalMekanik)
class JadwalMekanikAdmin(admin.ModelAdmin):
    list_display = ('mekanik', 'tanggal', 'jam_mulai', 'jam_selesai', 'tersedia')
    list_filter = ('tanggal', 'tersedia', 'mekanik')
    search_fields = ('mekanik__nama_lengkap',)
    fieldsets = (
        ('Mekanik & Tanggal', {
            'fields': ('mekanik', 'tanggal')
        }),
        ('Jam Kerja', {
            'fields': ('jam_mulai', 'jam_selesai')
        }),
        ('Status', {
            'fields': ('tersedia',)
        }),
    )
