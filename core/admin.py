from django.contrib import admin
from .models import Layanan, Mekanik, Kendaraan
from booking.admin import JadwalMekanikInline


@admin.register(Layanan)
class LayananAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis', 'harga_dasar', 'durasi_estimasi', 'is_active', 'created_at')
    list_filter = ('jenis', 'is_active', 'created_at')
    search_fields = ('nama', 'deskripsi')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Info Layanan', {
            'fields': ('nama', 'jenis', 'deskripsi')
        }),
        ('Harga & Durasi', {
            'fields': ('harga_dasar', 'durasi_estimasi')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Media', {
            'fields': ('gambar',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['activate_layanan', 'deactivate_layanan']
    
    def activate_layanan(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} layanan telah diaktifkan")
    activate_layanan.short_description = "Aktifkan layanan"
    
    def deactivate_layanan(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} layanan telah dinonaktifkan")
    deactivate_layanan.short_description = "Nonaktifkan layanan"


@admin.register(Mekanik)
class MekanikAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'spesialisasi', 'pengalaman', 'tersedia', 'is_active', 'created_at')
    list_filter = ('tersedia', 'is_active', 'created_at', 'spesialisasi')
    search_fields = ('nama_lengkap', 'user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    inlines = [JadwalMekanikInline]
    
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Info Mekanik', {
            'fields': ('nama_lengkap', 'spesialisasi', 'pengalaman')
        }),
        ('Status', {
            'fields': ('tersedia', 'is_active')
        }),
        ('Media', {
            'fields': ('foto',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_available', 'mark_unavailable', 'activate_mekanik', 'deactivate_mekanik']
    
    def mark_available(self, request, queryset):
        updated = queryset.update(tersedia=True)
        self.message_user(request, f"{updated} mekanik telah tersedia")
    mark_available.short_description = "Tandai sebagai tersedia"
    
    def mark_unavailable(self, request, queryset):
        updated = queryset.update(tersedia=False)
        self.message_user(request, f"{updated} mekanik tidak tersedia")
    mark_unavailable.short_description = "Tandai sebagai tidak tersedia"
    
    def activate_mekanik(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} mekanik telah diaktifkan")
    activate_mekanik.short_description = "Aktifkan mekanik"
    
    def deactivate_mekanik(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} mekanik telah dinonaktifkan")
    deactivate_mekanik.short_description = "Nonaktifkan mekanik"


@admin.register(Kendaraan)
class KendaraanAdmin(admin.ModelAdmin):
    list_display = ('nomor_plat', 'merk', 'model', 'jenis', 'pemilik', 'is_active', 'created_at')
    list_filter = ('jenis', 'tahun', 'is_active', 'created_at')
    search_fields = ('nomor_plat', 'merk', 'model', 'pemilik__username', 'pemilik__email')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Pemilik', {
            'fields': ('pemilik',)
        }),
        ('Info Kendaraan', {
            'fields': ('merk', 'model', 'tahun', 'jenis')
        }),
        ('Plat Nomor', {
            'fields': ('nomor_plat',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['activate_kendaraan', 'deactivate_kendaraan']
    
    def activate_kendaraan(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} kendaraan telah diaktifkan")
    activate_kendaraan.short_description = "Aktifkan kendaraan"
    
    def deactivate_kendaraan(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} kendaraan telah dinonaktifkan")
    deactivate_kendaraan.short_description = "Nonaktifkan kendaraan"
