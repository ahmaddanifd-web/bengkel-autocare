from django.contrib import admin
from .models import Booking, JadwalMekanik


class JadwalMekanikInline(admin.TabularInline):
    """Inline admin untuk JadwalMekanik di halaman Mekanik"""
    model = JadwalMekanik
    extra = 1
    fields = ('tanggal', 'jam_mulai', 'jam_selesai', 'tersedia', 'is_active')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'kendaraan', 'layanan', 'status', 'tanggal_booking', 'mekanik', 'created_at')
    list_filter = ('status', 'created_at', 'mekanik', 'layanan')
    search_fields = ('customer__username', 'customer__email', 'kendaraan__nomor_plat', 'keluhan')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'tanggal_booking'
    
    fieldsets = (
        ('Info Customer', {
            'fields': ('customer', 'kendaraan')
        }),
        ('Info Layanan & Mekanik', {
            'fields': ('layanan', 'mekanik', 'tanggal_booking')
        }),
        ('Keluhan & Catatan', {
            'fields': ('keluhan',)
        }),
        ('Status', {
            'fields': ('status', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_confirmed', 'mark_as_in_progress', 'mark_as_completed', 'mark_as_cancelled']
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='dikonfirmasi')
        self.message_user(request, f"{updated} booking telah dikonfirmasi")
    mark_as_confirmed.short_description = "Konfirmasi booking yang dipilih"
    
    def mark_as_in_progress(self, request, queryset):
        updated = queryset.update(status='diproses')
        self.message_user(request, f"{updated} booking sedang diproses")
    mark_as_in_progress.short_description = "Tandai sebagai sedang diproses"
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='selesai')
        self.message_user(request, f"{updated} booking telah selesai")
    mark_as_completed.short_description = "Tandai sebagai selesai"
    
    def mark_as_cancelled(self, request, queryset):
        updated = queryset.update(status='dibatalkan')
        self.message_user(request, f"{updated} booking telah dibatalkan")
    mark_as_cancelled.short_description = "Batalkan booking"


@admin.register(JadwalMekanik)
class JadwalMekanikAdmin(admin.ModelAdmin):
    list_display = ('mekanik', 'tanggal', 'jam_mulai', 'jam_selesai', 'tersedia', 'is_active', 'created_at')
    list_filter = ('tanggal', 'tersedia', 'is_active', 'mekanik')
    search_fields = ('mekanik__nama_lengkap',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'tanggal'
    
    fieldsets = (
        ('Mekanik & Tanggal', {
            'fields': ('mekanik', 'tanggal')
        }),
        ('Jam Kerja', {
            'fields': ('jam_mulai', 'jam_selesai')
        }),
        ('Status', {
            'fields': ('tersedia', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_available', 'mark_as_unavailable']
    
    def mark_as_available(self, request, queryset):
        updated = queryset.update(tersedia=True)
        self.message_user(request, f"{updated} jadwal telah tersedia")
    mark_as_available.short_description = "Tandai sebagai tersedia"
    
    def mark_as_unavailable(self, request, queryset):
        updated = queryset.update(tersedia=False)
        self.message_user(request, f"{updated} jadwal tidak tersedia")
    mark_as_unavailable.short_description = "Tandai sebagai tidak tersedia"
