import datetime

# Dapatkan tanggal dan waktu saat ini
today = datetime.datetime.now()

# Hitung akhir tahun 2025
end_of_year = datetime.datetime(2024, 12, 31)

# Hitunglah selisih kedua tanggal tersebut
difference = end_of_year - today

# Cetak jumlah hari, jam, menit, dan detik
print("Days:", difference.days)
print("Hours:", difference.seconds // 3600)
print("Minutes:", (difference.seconds // 60) % 60)
print("Seconds:", difference.seconds % 60)
