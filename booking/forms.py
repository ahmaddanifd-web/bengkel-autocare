from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    tanggal_booking = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
            'min': timezone.now().isoformat(),
        }),
        help_text="Pilih tanggal dan waktu untuk booking"
    )

    class Meta:
        model = Booking
        fields = ['kendaraan', 'layanan', 'tanggal_booking', 'keluhan']
        widgets = {
            'kendaraan': forms.Select(attrs={
                'class': 'form-control',
            }),
            'layanan': forms.Select(attrs={
                'class': 'form-control',
            }),
            'keluhan': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Jelaskan keluhan kendaraan Anda...',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        tanggal_booking = cleaned_data.get('tanggal_booking')
        
        if tanggal_booking and tanggal_booking <= timezone.now():
            raise ValidationError("Tanggal booking harus di masa depan")
        
        return cleaned_data

    def clean_kendaraan(self):
        kendaraan = self.cleaned_data.get('kendaraan')
        if kendaraan and not kendaraan.is_active:
            raise ValidationError("Kendaraan tidak tersedia untuk booking")
        return kendaraan

    def clean_layanan(self):
        layanan = self.cleaned_data.get('layanan')
        if layanan and not layanan.is_active:
            raise ValidationError("Layanan tidak tersedia saat ini")
        return layanan
