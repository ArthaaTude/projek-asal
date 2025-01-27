import os
import time
import random
import datetime
import pandas as pd
os.system("cls")

tanggal_bulan_hari = datetime.datetime.now()
riwayat_permainan = pd.DataFrame(columns=["Nama", "Level", "Kesalahan", "Permainan", "Total kesalahan"])
daftar_nama = []
nama = ""
def sesuai():
    def awal():
        while True:
            try:
                print(pertama, operasi, kedua)
                jawabb = int(input(f"Jawab {nama}:"))
                
                os.system("cls")
                print("0 Jawaban\nTidak ada batas waktu!!!")
                if jawabb == hasil:
                    os.system("cls")
                    print("Benar")
                    sesuai()
                elif jawabb == 0:
                    os.system("cls")
                    print(pertama, operasi, kedua,"=",hasil)
                    sesuai() 
                else:
                    print("Salah")
                    awal()
            except ValueError:
                os.system("cls")
                print("angka")
    while True:
        print("0.kembali\n1.Susah\n2.Gampang\n3.Sangat susah\n4.Hacker")
        tingkatan = (input("Tingkatan:"))
        os.system("cls")
        if tingkatan == "1":
            print("Susah",nama)
            pertama = random.randint(10,100)
            kedua = random.randint(10,100)
        elif tingkatan == "2":
            print("Gampang",nama)
            pertama = random.randint(1,15)
            kedua = random.randint(1,15)
        elif tingkatan == "0":
            stat()
        elif tingkatan == "3":
            print("Sangat susah",nama)
            pertama = random.randint(100,1000)
            kedua = random.randint(100,1000)
        elif tingkatan == "4":
            print("Hacker",nama)
            pertama = random.randint(10000,10000000)
            kedua = random.randint(10000,10000000)    
        else:
            sesuai()
        while True:
            print("0.Kembali\n1.Utama") 
            operasi = (input("Pilihan (+, -, x):"))

            if operasi in ['+', '-', 'x']:
                if operasi == "+":
                    hasil = pertama + kedua
                elif operasi == "-":
                    hasil = pertama - kedua
                elif operasi == "x":
                    hasil = pertama * kedua
                print("Tidak ada waktu")
                awal()
            elif operasi == "0":
                os.system("cls")  
                sesuai()
            elif operasi == "1":
                os.system("cls")
                stat()
            else:
                os.system("cls")
                continue
            
def main(kesulitan,selesai = True):
    def tambah():
        while True:
            tambah = (input("Mau nambah nama Y/T:"))
            
            if tambah == "y":
                ganti_nama()
                os.system("cls")
            elif tambah == "t":
                os.system("cls")
                tampilkan_daftar_nama()
                text()
                exit()
            else:
                pass                         
    def text():
        print(pertama,obsi,kedua,"=",hasil,"\nJawaban anda",jawab,nama)
        print("Tanggal:",tanggal_bulan_hari)
        data = pd.DataFrame({
            "Nama":[nama],
            "Level":[kesulitan],
            "Kesalahan":[kesalahan],
            "Permainan":[permainan],
            "Total kesalahan":[total_kesalahan]
        })
        global riwayat_permainan
        # membuat tambah nama table dan stastistik permainan
        if not ((riwayat_permainan["Nama"] == nama) & (riwayat_permainan["Level"] == kesulitan)).any():
            riwayat_permainan = pd.concat([riwayat_permainan, data], ignore_index=True)
        print(riwayat_permainan)
    def soal():
        nonlocal permainan_dimulai
        if kesulitan:
            while True:
                print("0.Kembali\n1.Mulai\n2.Mulai tanpa jeda\nLevel",kesulitan,"\nPermainan anda",permainan,"\nTotal kesalahan",total_kesalahan)
                siap = (input(f"Siap {nama}:"))                
                if siap == "1":
                    break
                elif siap == "0":
                    os.system("cls")
                    stat()
                elif siap == "2":
                    return True
                else:
                    os.system("cls")
                return False
    permainan = 0
    total_kesalahan = 0
    benar = 0
    total_ganti = 0
    permainan_dimulai = False
    while selesai:
        waktu = 6 if kesulitan != "sulit" else 30
        mulai = time.time()
        pertama = random.randint(1,10 if kesulitan == "gampang" else 100)
        kedua = random.randint(1,10 if kesulitan == "gampang" else 100)
        obsi = random.choice("x+-")
        kesalahan = 0
        kekalahan = 4
        ganti = 2
        if kesulitan == "sangat sulit":
            if not permainan_dimulai:
                permainan_dimulai = soal()
            waktu = 60
            mulai = time.time()
            pertama = random.randint(100,1000)
            kedua = random.randint(100,1000)
        elif kesulitan == "hacker":
            soal()
            waktu = 300
            mulai = time.time()
            pertama = random.randint(10000,10000000)
            kedua = random.randint(10000,10000000)
        elif kesulitan == "sulit" or kesulitan in "gampang":
            if not permainan_dimulai:
                permainan_dimulai = soal()
            mulai = time.time()
        elif kesulitan == "kuis":
            if not permainan_dimulai:
                permainan_dimulai = soal()
            waktu = 6
            mulai = time.time()
            pertama = random.randint(1,10)
            kedua = random.randint(1,10)
        os.system("cls")
        while selesai:
            print("level",kesulitan)
            print(pertama,obsi,kedua,"= ?")
            sisa_waktu = int(waktu - (time.time() - mulai))
            print(f"Sisa waktu: {sisa_waktu} detik")
            try:
                jawab = int(input(f"Jawab {nama}:"))
                
                if obsi == "+":
                    hasil = pertama+kedua
                elif obsi == "-":
                    hasil = pertama-kedua
                elif obsi == "x":
                    hasil = pertama*kedua
                
                os.system("cls")
                if sisa_waktu <= 0:
                    print("Lambat Menjawab soal!!!")
                    text()
                    tambah()
                    os.system("cls")
                elif jawab == hasil:
                    print("benar")
                    permainan += 1
                    benar += 1
                    # kuis error 
                    if kesulitan == "kuis":
                        if benar == 1:
                            kesulitan = "gampang"
                        elif benar == 2:
                            kesulitan = "sulit"
                        elif benar == 3:
                            kesulitan = "sangat sulit"
                        else:
                            while True:
                                lagi = (input(f"Lagi kuis {nama} Y?T:"))
                                
                                if lagi == "y":
                                    os.system("cls")
                                    if kesulitan == "sangat sulit":
                                        os.system("cls")
                                        main("kuis")
                                    break       
                                elif lagi == "t":
                                    os.system("cls")
                                    print("Selamat Anda Menang Kuis",nama)    
                                    text()
                                    ganti_nama()
                                    exit()
                                else:
                                    pass
                    break        
                elif time.time() - mulai > waktu:
                    print("Waktu habis.",waktu,"detik")
                    text()
                    while selesai:
                        lanjut = (input("Lanjut Y?T:"))
                        
                        if lanjut == "y":
                            stat()
                        elif lanjut == "t":   
                            os.system("cls")
                            text()
                            tambah()
                        else:
                            os.system("cls")
                            text()
                elif jawab == hasil:
                    mulai = time.time()    
                else:
                    kesalahan += 1
                    kekalahan -= 1
                    total_kesalahan += 1
                    ganti -= 1
                    total_ganti += 1
                    os.system("cls")
                    print("Kesalahan anda",kesalahan)
                    
                    if jawab > ganti:
                        print("1.Ganti soal")
                        if jawab == 1:
                            os.system("cls")
                            break
                        elif total_ganti >= 8:
                            os.system("cls")
                            print("Terlalu Banyak Salah",nama)
                            text()
                            tambah()
                    if jawab > kekalahan:
                        if jawab == 0:
                            while selesai:
                                os.system("cls")
                                yakin = (input(f"Yakin Menyerah {nama} Y/T:"))
                                
                                if yakin == "y":
                                    os.system("cls")
                                    print("Anda menyerah",nama)
                                    text()
                                    while selesai:
                                        nyerah = (input("Lagi Main Y/T:"))
                                        
                                        if nyerah == "t":
                                            os.system("cls")
                                            print("Anda menyerah",nama)
                                            text()
                                            tambah()
                                        elif nyerah == "y":
                                            os.system("cls")
                                            stat()
                                        else:
                                            pass      
                                elif yakin == "t":
                                    os.system("cls")
                                    soal()
                                    break
                                else:
                                    pass
                        else:
                            print("0.Untuk Menyerah")       
                    else:
                        pass        
            except ValueError:
                os.system("cls")
                print("Kesalahan anda",kesalahan)
def stat():
    print("Waktu sudah di sesuaikan level untuk menjawab.\nMatematika")
    while True:
        print("0.keluar\n1.Gampang\n2.Sulit\n3.Sangat sulit\n4.hacker\n5.Sesuaikan\n6.Kuis")
        try:
            pilihan = int(input("Pilihan:"))

            os.system("cls")
            if pilihan == 1:
                main("gampang")
            elif pilihan == 2:
                main("sulit")
            elif pilihan == 3:
                main("sangat sulit")
            elif pilihan == 0:
                os.system("cls")
                print(nama,"Keluar")
                tampilkan_daftar_nama()
                exit()
            elif pilihan == 4:
                main("hacker")
            elif pilihan == 5:
                sesuai()
            elif pilihan == 6:
                main("kuis")
            else:
                print("Tidak ada pilihan",pilihan)
        except ValueError:
            os.system("cls")
            print("Angka")
def tampilkan_daftar_nama():
    print("Daftar Nama Terdaftar:")
    for index, nama in enumerate(daftar_nama, start=1):
        print(f"{index}. {nama}")
def ganti_nama():
    global nama
    while True:
        nama_baru = input("Nama:").capitalize()
        if len(nama_baru) >= 10:
            jumlah = len(nama_baru)
            print(f"Nama terlalu panjang {jumlah} karakter")
        elif not nama_baru.replace(" ","").isalpha():
            print("Gagal")
        elif len(nama_baru) <= 2:
            os.system("cls")
            pass
        elif nama_baru == nama:
            print("Nama baru tidak boleh sama dengan nama sebelumnya.") 
        else:
            nama = nama_baru
            daftar_nama.append(nama)
            stat()
ganti_nama()