# Sistem Perpustakaan (MVC - Python & CustomTkinter)

## 1. Deskripsi Singkat Aplikasi
Sistem Perpustakaan adalah aplikasi desktop berbasis Python yang dirancang menggunakan arsitektur Model-View-Controller (MVC) untuk mengelola data buku, peminjaman, dan otentikasi petugas perpustakaan secara efisien dengan antarmuka grafis modern menggunakan CustomTkinter serta database MySQL.

## 2. Struktur Direktori MVC
- `config/` : Konfigurasi koneksi database MySQL
- `controllers/` : Logika pengendali alur aplikasi
- `models/` : Pengolahan data dan query database
- `views/` : Antarmuka pengguna (GUI) CustomTkinter
- `tests/` : Unit testing menggunakan pytest
- `dist/` : Berkas eksekusi mandiri (.exe) hasil build PyInstaller

## 3. Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan Python dan MySQL (Laragon) aktif di komputer Anda.
2. Buat database baru untuk sistem perpustakaan.
3. Instal seluruh pustaka yang diperlukan dengan menjalankan perintah berikut di terminal:
   ```bash
   pip install -r requirements.txt