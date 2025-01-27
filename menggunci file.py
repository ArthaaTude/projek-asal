# menggunci file
import random
import zipfile
import os

def shuffle_password(password):
    # Mengonversi password menjadi daftar karakter
    password_list = list(password)
    # Mengacak urutan karakter dalam password
    random.shuffle(password_list)
    # Menggabungkan karakter yang sudah diacak menjadi string baru
    shuffled_password = ''.join(password_list)
    return shuffled_password

def encrypt_zip_file(file_path, password):
    # Membuat nama file terenkripsi dengan menambahkan ekstensi ".enc" ke file asli
    encrypted_file = file_path + '.enc'
    # Membuat file terenkripsi
    with open(file_path, 'rb') as f_in:
        with open(encrypted_file, 'wb') as f_out:
            f_out.write(f_in.read())
    # Membuka file arsip
    with zipfile.ZipFile(encrypted_file, 'a') as zip_file:
        # Mengenkripsi file dengan password yang sudah diacak
        zip_file.setpassword(bytes(shuffle_password(password), 'utf-8'))
    # Menghapus file asli
    os.remove(file_path)

# Ganti dengan nama file arsip yang ingin Anda enkripsi
file_path = 'percobbaan.rar'
# Ganti dengan password yang ingin Anda gunakan untuk mengenkripsi file
password = '12345678'

# Mengenkripsi file arsip dengan password yang sudah diacak
encrypt_zip_file(file_path, password)
