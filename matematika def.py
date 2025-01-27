import os
def hitung_luas():
    print("Hitung Luas")
    waktu = float(input("Luas:"))
    jarak = float(input("Jarak:"))
    kecepatan = waktu * jarak
    print("Kecepatan:",kecepatan)
def segitiga_luas():
    print("Segitiga Luas")
    alas = float(input("Alas:"))
    tinggi = float(input("Segitiga:"))
    luas = 0.5 * (alas * tinggi)
    print("Luas Pesergi Panjang Adalah:",luas)
def luas_balok():
    print("Luas Blok")
    panjangg = float(input("Panjang:"))
    lebar = float(input("Lebar:"))
    tinggi = float(input("Tinggi:"))
    luas = (2*panjangg*lebar) + (2*panjangg*tinggi) + (2*lebar*tinggi)  
    print("Luas Balok Adalah:",luas)
def luas_bola():
    print("Luas Bola")
    jari = float(input("Jari Jari:"))
    luas = 4 * 3.14 * (jari**2)
    print("Luas Bola Adalah:",luas)
def tambah():
    print("Tambah")
    pertama = int(input("Pertama:"))    
    kedua = int(input("Kedua:"))
    ditambah = pertama+kedua
    print("Hasilnya Di Tambah",ditambah)
def kurang():
    print("kurang")
    pertama = int(input("Pertama:"))    
    kedua = int(input("Kedua:"))
    ditambah = pertama-kedua
    print("Hasilnya Di Kurang",ditambah)
def bagi():
    try:
        print("Bagi")
        pertama = float(input("Pertama:"))    
        kedua = float(input("Kedua:"))
        ditambah = pertama/kedua
        print("Hasilnya Di Bagi",ditambah)
    except ZeroDivisionError:
        print("Tidak Bisa Di Bagi 0")
def kali():
    print("Kali")
    pertama = int(input("Pertama:"))    
    kedua = int(input("Kedua:"))
    ditambah = pertama*kedua
    print("Hasilnya Di Kali",ditambah)
    if pertama <= 0 and kedua <= 0:
        print("Tidak Bisa Di Kali 0")  
while True:
    try:
        print("1.Hitung Luas\n2.Luas Segitiga\n3.Luas Blok\n4.Luas Bola \n5.Tambah\n6.Kurang\n7.Bagi\n8.Kali\n0.Keluar")
        pilihan = int(input("Pilihan Rumus:"))
        os.system("cls")
        if pilihan >= 9:
            print("Lebih")
        elif pilihan == 1:
            hitung_luas()
        elif pilihan == 2:
            segitiga_luas()
        elif pilihan == 3:
            luas_balok()
        elif pilihan == 4:
            luas_bola()
        elif pilihan == 5:
            tambah()
        elif pilihan == 6:
            kurang()
        elif pilihan == 7:
            bagi()
        elif pilihan == 8:
            kali()    
        else:
            break
    except ValueError:
        print("Hanya Angka")