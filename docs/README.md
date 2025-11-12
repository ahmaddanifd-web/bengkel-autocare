# 🚗 Bengkel AutoCare - Automotive Workshop Booking System

Sistem booking workshop otomotif modern dan responsif dengan Django 4.2+, Bootstrap 5, dan integrasi pembayaran Midtrans.

## 📋 Fitur

- ✅ **Manajemen Layanan** - Tambah, edit, kelola jenis layanan perbaikan
- ✅ **Manajemen Mekanik** - Data mekanik dengan spesialisasi dan jadwal kerja
- ✅ **Booking Kendaraan** - Pelanggan dapat memesan layanan dengan mudah
- ✅ **Jadwal Mekanik** - Kelola jadwal ketersediaan mekanik real-time
- ✅ **Sistem Pembayaran** - Integrasi Midtrans untuk pembayaran online aman
- ✅ **Admin Dashboard** - Dashboard lengkap untuk mengelola semua data
- ✅ **Responsive UI** - Antarmuka modern dengan Bootstrap 5 & Icons
- ✅ **Authentication** - Login/logout dengan Django auth system
- ✅ **History Tracking** - Riwayat booking dan status real-time

## 🏗️ Struktur Proyek

```
bengkel_autocare/
├── manage.py                      # Django management
├── requirements.txt               # Dependencies
├── README.md                      # Documentation
│
├── bengkel/                       # Project config
│   ├── __init__.py
│   ├── settings.py                # Settings
│   ├── urls.py                    # URLs
│   ├── wsgi.py                    # WSGI
│
├── core/                          # Layanan, Mekanik, Kendaraan
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── booking/                       # Booking & Jadwal
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── payment/                       # Pembayaran
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── templates/                     # HTML Templates
│   ├── base.html
│   ├── home.html
│   ├── booking_form.html
│   ├── booking_success.html
│   └── payment_page.html
│
├── static/                        # CSS, JS, Images
│
├── media/                         # User uploads
│
└── db.sqlite3                     # Database
```

## 🚀 Quick Start

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Konfigurasi Database & Migrasi

```powershell
python manage.py migrate
python manage.py createsuperuser
```

### 3. Jalankan Development Server

```powershell
python manage.py runserver
```

Server akan berjalan di `http://127.0.0.1:8000/`

### 4. Akses Admin Dashboard

Buka http://127.0.0.1:8000/admin/ dan login dengan akun superuser.

## 📚 Database Models

### Core App
- **Layanan**: Jenis layanan perbaikan
  - nama, jenis, deskripsi, harga_dasar, durasi_estimasi, gambar

- **Mekanik**: Data mekanik
  - user, nama_lengkap, spesialisasi, pengalaman, foto, tersedia

- **Kendaraan**: Data kendaraan pelanggan
  - pemilik, merk, model, tahun, nomor_plat, jenis

### Booking App
- **Booking**: Pesanan servis
  - customer, kendaraan, layanan, mekanik, tanggal_booking, keluhan, status, created_at

- **JadwalMekanik**: Jadwal kerja
  - mekanik, tanggal, jam_mulai, jam_selesai, tersedia

### Payment App
- **Transaksi**: Pembayaran
  - booking, kode_transaksi, total_biaya, metode_pembayaran, status, waktu_transaksi, waktu_kadaluarsa

## 🔑 Setup Midtrans

1. Daftar di https://midtrans.com
2. Dapatkan Server Key dan Client Key
3. Update di `bengkel/settings.py`:
   ```python
   MIDTRANS_SERVER_KEY = 'your-server-key'
   MIDTRANS_CLIENT_KEY = 'your-client-key'
   ```

## 📌 URL Routes

```
Homepage:       http://localhost:8000/
Booking:        http://localhost:8000/booking/
Payment:        http://localhost:8000/payment/
Admin:          http://localhost:8000/admin/
Accounts:       http://localhost:8000/accounts/
```

## 🛠️ Troubleshooting

| Error | Solusi |
|-------|--------|
| ModuleNotFoundError | Run `pip install -r requirements.txt` |
| DisallowedHost | Update ALLOWED_HOSTS di settings.py |
| Database Error | Run `python manage.py migrate` |
| Static Files Missing | Run `python manage.py collectstatic` |

## 🔐 Production Checklist

- [ ] Set `DEBUG = False` di production
- [ ] Gunakan environment variables untuk keys
- [ ] Aktifkan HTTPS
- [ ] Gunakan database production (PostgreSQL)
- [ ] Set SECRET_KEY yang kuat
- [ ] Update ALLOWED_HOSTS
- [ ] Enable CSRF protection
- [ ] Setup backup database
- [ ] Configure email backend
- [ ] Setup monitoring & logging

## 📞 Support

- Email: info@bengkel.local
- Phone: (021) 300-1234

## 📄 License

Copyright © 2025 Bengkel AutoCare. All rights reserved.

---

**Version:** 1.0.0 | **Last Updated:** November 12, 2025
