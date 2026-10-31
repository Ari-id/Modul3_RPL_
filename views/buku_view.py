import customtkinter as ctk
from tkinter import ttk

# Atur mode tampilan ke Terang (Light Mode)
ctk.set_appearance_mode("light")


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Data Buku")
        self.geometry("800x500")

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT BUKU
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Komponen Input
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku"
        )
        self.entry_judul.pack(pady=8, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis"
        )
        self.entry_penulis.pack(pady=8, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit (Misal: 2024)"
        )
        self.entry_tahun.pack(pady=8, padx=15, fill="x")

        # Tombol Simpan (Hijau)
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green"
        )
        self.btn_simpan.pack(pady=(15, 5), padx=15, fill="x")

        # Tombol Perbarui Data (Biru)
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="#1f538d"
        )
        self.btn_update.pack(pady=5, padx=15, fill="x")

        # Tombol Hapus Data (Merah)
        self.btn_delete = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="#c0392b"
        )
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # ==========================================
        # TAMBAHAN UNTUK TUGAS 3: Tombol Logout
        # ==========================================
        self.btn_logout = ctk.CTkButton(
            self.frame_kiri,
            text="Logout",
            fg_color="gray"
        )
        self.btn_logout.pack(pady=(15, 5), padx=15, fill="x")


        # FRAME KANAN: TABEL DAFTAR BUKU
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Tabel Treeview
        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("judul", width=180)
        self.tabel.column("penulis", width=120)
        self.tabel.column("tahun", width=60, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()