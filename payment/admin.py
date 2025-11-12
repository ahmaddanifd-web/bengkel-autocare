from django.contrib import admin
from .models import Transaksi


@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('kode_transaksi', 'booking', 'total_biaya', 'metode_pembayaran', 'status', 'created_at')
    list_filter = ('status', 'metode_pembayaran', 'created_at')
    search_fields = ('kode_transaksi', 'booking__id', 'booking__customer__username')
    readonly_fields = ('kode_transaksi', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Booking & Kode', {
            'fields': ('booking', 'kode_transaksi')
        }),
        ('Biaya', {
            'fields': ('total_biaya',)
        }),
        ('Pembayaran', {
            'fields': ('metode_pembayaran', 'status', 'is_active')
        }),
        ('Midtrans', {
            'fields': ('midtrans_token',),
            'classes': ('collapse',)
        }),
        ('Waktu', {
            'fields': ('created_at', 'updated_at', 'waktu_kadaluarsa'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_paid', 'mark_as_failed', 'mark_as_pending', 'mark_as_expired']
    
    def mark_as_paid(self, request, queryset):
        updated = queryset.update(status='paid')
        self.message_user(request, f"{updated} transaksi telah ditandai sebagai terbayar")
    mark_as_paid.short_description = "Tandai sebagai terbayar"
    
    def mark_as_failed(self, request, queryset):
        updated = queryset.update(status='failed')
        self.message_user(request, f"{updated} transaksi ditandai gagal")
    mark_as_failed.short_description = "Tandai sebagai gagal"
    
    def mark_as_pending(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f"{updated} transaksi dalam status pending")
    mark_as_pending.short_description = "Tandai sebagai pending"
    
    def mark_as_expired(self, request, queryset):
        updated = queryset.update(status='expired')
        self.message_user(request, f"{updated} transaksi kadaluarsa")
    mark_as_expired.short_description = "Tandai sebagai kadaluarsa"
