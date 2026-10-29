from unittest.mock import MagicMock
from models.buku_model import BukuModel

# --- KODE AWAL ANDA (Uji Coba Manual) ---
model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


# --- TAMBAHAN KODE UNTUK SOAL NO. 3 (Unit Test dengan pytest) ---
def test_get_all_buku():
    # Menginisialisasi Model untuk testing
    test_model = BukuModel()
    
    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    test_model.conn = MagicMock()
    mock_cursor = MagicMock()
    test_model.conn.cursor.return_value = mock_cursor
    
    # Menentukan data tiruan (mock data) yang dikembalikan oleh database
    mock_cursor.fetchall.return_value = [
        {"id_buku": 1, "judul": "Pemrograman Python MVC", "penulis": "Guido van Rossum", "tahun_terbit": 2023},
        {"id_buku": 2, "judul": "Struktur Data", "penulis": "Andi", "tahun_terbit": 2024}
    ]
    
    # Menjalankan fungsi get_all_buku yang diuji
    hasil = test_model.get_all_buku()
    
    # Memverifikasi hasil pengujian
    assert len(hasil) == 2
    assert hasil[0]["judul"] == "Pemrograman Python MVC"
    
    # Memverifikasi apakah kursor benar-benar mengeksekusi query database
    mock_cursor.execute.assert_called_once()