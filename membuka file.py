# membuka file
import zipfile

def decrypt_zip_file(file_path, password):
    # Membuka file arsip terenkripsi
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        # Mencoba untuk mengekstrak isi file arsip dengan password yang diberikan
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            print("File arsip berhasil didekripsi.")
        except Exception as e:
            print("Gagal membuka file arsip. Pastikan password yang dimasukkan benar.")

# Ganti dengan nama file arsip yang ingin Anda dekripsi
file_path = 'percobbaan.rar.enc'
# Ganti dengan password asli yang digunakan saat mengenkripsi file
password = '12345678'

# Membuka kembali file arsip dengan password yang sesuai
decrypt_zip_file(file_path, password)
