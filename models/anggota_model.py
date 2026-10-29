import mysql.connector

class AnggotaModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all_anggota(self):
        self.cursor.execute("SELECT * FROM anggota")
        return self.cursor.fetchall()

    def create_anggota(self, nama, alamat):
        try:
            # Diubah dari 'nama_anggota' menjadi 'nama' sesuai kolom database
            query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
            self.cursor.execute(query, (nama, alamat))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    