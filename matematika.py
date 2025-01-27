import os
mulai = True
while mulai:
    try:
        pilihan = int(input(" 1.Hitung Kecepatan \n 2.Luas Segitiga \n 3.Luas Blok \n 4.Luas Bola \n 5.Tambah \n 6.Kurang \n 7.Bagi \n 8.Kali \n 0.Keluar \n Pilihan Rumus:"))
        os.system("cls")
    except ValueError:
        print("Hanya Angka")
    if pilihan == 1:
        while mulai:
            try:
                print("Hiting Kecepatan")
                jarak = float(input("Jarak:"))
                waktu = float(input("Waktu:"))
                kecepatan = jarak * waktu
                print("Kecepatan:",kecepatan)
                if pilihan:
                    mulai = False
            except ValueError:
                print("Nomer 1 Hanya Angka")
    elif pilihan == 0:
        break
    elif pilihan >= 9:
        print("Lebih")
    elif pilihan == 2:
        while mulai:
            try:
                print("Luas Segitiga")
                alas = float(input("Luas:"))    
                tinggi = float(input("Segitiga:"))
                luas = 0.5 * (alas * tinggi)
                print("Luas Segitiga Adalah:",luas)
                if pilihan:
                    mulai = False
            except ValueError:
                print("Nomer 2 Hanya Angka")
    elif pilihan == 3:
        while True:
            try:
                print("Luas Blok")
                panjangg = float(input("Panjang:"))           
                lebar = float(input("Lebar:"))           
                tinggi = float(input("Tinggi:"))
                luas = (2*panjangg*lebar) + (2*panjangg*tinggi) + (2*lebar*tinggi)
                print("Luas Balok Adalah:",luas)
                if pilihan:
                    mulai = False
                    break
            except ValueError:
                print("Nomer 3 Hanya Angka")
    elif pilihan == 4:
        while True:
            try:
                print("Luas Bola")
                jari = float(input("Jari Jari:"))
                luas = 4 * 3.14 * (jari**2)
                print("Luas Bola Adalah",luas)
                if pilihan:
                    mulai = False
                    break
            except ValueError:
                print("Hanya Angka")
    elif pilihan == 5:
        while mulai:
            try:
                print("Tambah")
                tambah = int(input("Pertama:"))            
                kedua = int(input("Kedua:"))
                ditambah = tambah+kedua
                print("hasilnya Di Tambah",ditambah)
                if pilihan:
                    mulai = False
            except ValueError:
                print("Hanya Angka")
    elif pilihan == 6:
        while mulai:
            try:
                print("Kurang")
                tambah = int(input("Pertama:"))            
                kedua = int(input("Kedua:"))
                ditambah = tambah-kedua
                print("Hasilnya Di Kurang ",ditambah)
                if pilihan:
                    mulai = False
            except ValueError:
                print("Hanya Angka")
    elif pilihan == 7:
        while mulai:
            try:
                print("bagi")
                tambah = float(input("Pertama:"))            
                kedua = float(input("Kedua:"))
                ditambah = tambah/kedua
                print("Hasilnya Di Bagi",ditambah)
                if pilihan:
                    mulai = False
            except ZeroDivisionError:
                print("Tidak Bisa Di Bagi 0")
    elif pilihan == 8:
        while mulai:
            try:
                print("Kali")
                tambah = int(input("Pertama:"))            
                kedua = int(input("Kedua:"))
                ditambah = tambah*kedua
                print("hasilnya Di Kali",ditambah)
                if tambah <= 0 and kedua <= 0:
                    print("Tidak Bisa Di Kali 0")
                elif pilihan:
                    mulai = False    
            except ValueError:
                print("Hanya Angka")