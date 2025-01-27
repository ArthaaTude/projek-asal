import os
import time
import random
os.system("cls")

waktu = 30
mulai = time.time()
def main(acak,data = 0,salah = 0,kalah = 3,tambahkan = []):
    print(f"Selamat Datang Di Kopetensi Matematika {nama}")
    while True:
        try:
            print("0.Kembali")
            berapa = int(input("Berapa Kali:"))
            mulai = time.time()
            os.system("cls")
            if berapa == 0:
                persiapan()
            elif berapa >= 1000:
                print(f"Banyak Sekali {berapa}")
                break
            elif berapa <= 2:
                print(f"Terlalu sedikit {berapa}")
                break
            while True:
                for _ in range(berapa):
                    nomer = random.randint(*acak)
                    tambahkan.append(nomer)
                    data += nomer
                    print(nomer)
                    time.sleep(2)
                    os.system("cls")
                    print("+")
                    mulai = time.time()
                    
                os.system("cls")
                while True:
                    if time.time() - mulai > waktu:
                        print(f"waktu habis\n{tambahkan} = {data}\nHasil: {data}\nNama: {nama}")
                        coba_lagi()
                    try:
                        jawab = int(input(f"Jawab {nama}:"))
                        os.system("cls")
                        if jawab == data:
                            tambahkan.clear()
                            print(f"Benar")
                            mulai = time.time()
                            main((1,100))
                        else:
                            salah += 1
                            os.system("cls")
                            print(f"Salah {salah}")
                            kalah -= 1
                            if kalah < 1:
                                print(f"{tambahkan} = {data}\nHasil: {data}\nNama: {nama}")
                                tambahkan.clear()
                                coba_lagi()
                    except ValueError:
                        pass
        except ValueError:
            pass
def persiapan():
    while True:
        print("0.Kembali\n1.Belajar\n2.Contoh\n3.Latihan\n4.Bermain")
        pilihh = (input("Pilih:"))
        os.system("cls")
        if pilihh == "0":
            break
        elif pilihh == "1":
            belajar()
        elif pilihh == "2":
            print("Contoh")
            main((1,1))
        elif pilihh == "3":
            print("Latihan")
            main((1,10))
        elif pilihh == "4":
            print("Sulit")
            main((1,100))    
        else:
            pass
def belajar(data = 0,masukkan = 0):
    print("Mode Belajar")
    tambahkan = []
    while True:
        print("0.Pilihan")
        try:
            ulang = int(input("Berapa Kali:"))
            
            masukkan += 1
            os.system("cls")
            if masukkan >= 6:
                tambahkan.clear()
                persiapan()
            elif ulang == 0:
                persiapan()
            elif ulang >= 1000:
                print(f"Terlalu Banyak {ulang}")
            elif ulang <= 2:
                print(f"Terlalu Sedikit {ulang}")
            else:
                for _ in range(ulang):
                    acak = random.randint(1,10)
                    tambahkan.append(acak)
                    data += acak
                    print(acak)
                print(f"{tambahkan} = {data}\nHasil: {data}")
        except ValueError:
            pass
def coba_lagi():
    while True:
        lagi = (input("Lagi (Y/T):"))
        os.system("cls")
        if lagi.upper() == "Y":
            persiapan()
        elif lagi.upper() == "T":
            nama_baru()
        else:
            pass
def ingat_nomer(benar = 0):
    print("0.Kembali")
    while True:
        try:
            berapa_nomer = int(input("Nomer:"))
            if berapa_nomer >= 100:
                print(f"Terlalu Banyak {berapa_nomer}")
            elif berapa_nomer == 0:
                os.system("cls")
                persiapan()    
            elif berapa_nomer <= 10:
                print(f"Selalu Sedikit {berapa_nomer}")
            else:
                simpan_nomer = []
                for item in range(1,berapa_nomer + 1):
                    nomer_acak = random.randint(1,100)
                    time.sleep(3)
                    os.system("cls")
                    simpan_nomer.append(nomer_acak)
                    print(f"Nomer ke {item}: {nomer_acak}")
                os.system("cls")
                urutan_index = list(range(1,berapa_nomer + 1))
                random.shuffle(urutan_index)
                for data in urutan_index:
                    try:
                        print("0.Nyerah")
                        nomer = int(input(f"Nomer {data}:"))
                        os.system("cls")
                        if nomer == simpan_nomer[data-1]:
                            benar += 1
                            print(f"Anda Benar {benar}")
                        elif nomer == 0:
                            for x,y in enumerate(simpan_nomer ,start=1):
                                print(f"Nomer ke {x}: {y}")
                            coba_lagi()
                        else:
                            print("Salah")
                    except ValueError:
                        pass 
                break
        except ValueError:
            pass        
def menu():
    while True:
        print("0.Keluar\n1.Bermain\n2.Ingat nomer")
        pilihan = (input("Pilihan:"))
        mulai = time.time()
        os.system("cls")
        if pilihan == "0":
            print(f"Keluar {nama}")
            exit()
        elif pilihan == "1":
            persiapan()
        elif pilihan == "2":
            ingat_nomer()
        elif pilihan == "3":
            nama_baru()    
        else:
            print(f"Tidak ada pilihan {pilihan}")
        return mulai
def nama_baru():
    global nama
    while True:
        nama = (input("Nama:")).capitalize()
        if not nama.replace(" ","").isalpha() or len(nama) <= 2 or len(nama) >= 6:
            print("Gagal")
        else:
            os.system("cls")
            menu()
nama_baru()            