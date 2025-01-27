print("==========SELAMAT DATANG DI BIOSKOP!!!==========")
while True:
    try:
    # arti try:    
    # Blok kode yang mungkin menimbulkan pengecualian    
    # Misalnya, operasi yang berpotensi menghasilkan error
    # seperti pembagian dengan nol atau konversi tipe data yang tidak valid
    # Jika terjadi error, pengecualian akan dibangkitkan
    # dan pengeksekusian kode akan beralih ke blok except yang cocok. 
        umur=int(input("MASUKKAN UMUR KAMU:"))
        
        # mulai percabangan / perulangan
        if umur < 0 :
            print("GAGAL")   
        elif 0 <= umur < 17:# 0 sampai <= 17 tahun 
            print("UMUR ANDA ADALAH",umur,"GAK BOLEH MENGIKUTI ACARA INI")
        elif 17 <= umur < 120:# 17 sampai <= 120 tahun 
            print("UMUR ANDA ADALAH",umur,"BISA MENGIKUTI ACARA INI")
        # hakir percabangan    
        else:
            print("MELEBI KAPASITAS",umur)
        nama=(input("MASUKKAN NAMA ANDA:"))
        print("NAMA ANDA ADALAH",nama,"HELLO",nama)                
        break # Berhenti dari loop setelah menampilkan pesan kesalahan
    except ValueError: # Pengguna harus memasukkan text karena berupa nama variable int artinya bilangan bulat 
        print("HANYA ANGKA!!!")
        
        