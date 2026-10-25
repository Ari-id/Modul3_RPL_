from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model[cite: 4]
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli[cite: 4]
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi[cite: 4]
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True[cite: 4]
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil[cite: 4]
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil[cite: 4]
    model.conn.commit.assert_called_once()