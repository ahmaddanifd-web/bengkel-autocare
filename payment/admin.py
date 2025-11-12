from django.contrib import admin
from .models import Transaksi


@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('kode_transaksi', 'booking', 'total_biaya', 'metode_pembayaran', 'status')
    list_filter = ('status', 'metode_pembayaran', 'waktu_transaksi')
    search_fields = ('kode_transaksi', 'booking__id')
    readonly_fields = ('kode_transaksi', 'waktu_transaksi')
    fieldsets = (
        ('Booking & Kode', {
            'fields': ('booking', 'kode_transaksi')
        }),
        ('Biaya', {
            'fields': ('total_biaya',)
        }),
        ('Pembayaran', {
            'fields': ('metode_pembayaran', 'status', 'midtrans_token')
        }),
        ('Waktu', {
            'fields': ('waktu_transaksi', 'waktu_kadaluarsa'),
            'classes': ('collapse',)
        }),
    )
