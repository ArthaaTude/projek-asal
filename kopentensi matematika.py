import os
import time
import random
os.system("cls")

waktu = 4
mulai = time.time()
def main(acak):
    print("Selamat datang di kopetensi matematika")
    permainan = 0
    data = 0
    salah = 0
    nyerah = 3
    while True:
        try:
            print("0.Kembali")
            berapa = int(input("Berapa Kali:"))
            mulai = time.time()
            os.system("cls")
            if berapa == 0:
                break
            elif berapa >= 1000:
                print("Banyak Sekali")
                break
            elif berapa <= 2:
                print("Terlalu sedikit")
                break
            while True:
                print("0.kembali")
                pilih = (input("Pilih (+-x):"))
                
                os.system("cls")
                mulai = time.time()
                if pilih == "+":
                    for _ in range(berapa):
                        nomer = random.randint(*acak)
                        data += nomer
                        print(nomer)
                        time.sleep(1)
                        os.system("cls")
                        print("+")
                elif pilih == "-":
                    for _ in range(berapa):
                        nomer = random.randint(*acak)
                        data -= nomer
                        print(nomer)
                        time.sleep(1)
                        os.system("cls")
                        print("-")
                elif pilih == "x":
                    for _ in range(berapa):
                        nomer = random.randint(*acak)
                        data *= nomer
                        print(nomer)
                        time.sleep(1)
                        os.system("cls")
                        print("x")
                elif pilih == "0":
                    break        
                else:
                    continue
                mulai = time.time()
                    
                os.system("cls")
                while True:
                    if time.time() - mulai > waktu:
                        print("waktu habis")
                        print(f"Permainan {permainan}")
                        exit()
                    jawab = int(input("jawab:"))
                    
                    if jawab == data:
                        print(f"benar")
                        permainan += 1
                        print(f"jawaban tadi akan di {pilih} ke soal berikutnya")
                        time.sleep(2)
                        main((1,1))
                        mulai = time.time()
                    else:
                        salah += 1
                        os.system("cls")
                        print(f"Salah: {salah}\nPermainan {permainan}")
                        nyerah -= 1
                        if nyerah < 1:
                            print(f"Hasil: {data}")
                            return True
        except ValueError:
            pass
def persiapan():
    while True:
        print("1.Contoh\n2.Latihan\n3.Bermain\n4.Cara bermain\nt.kembali")
        siap = (input("Siap:"))
        os.system("cls")
        if siap == "1":
            main((1,1))
        elif siap == "2":
            main((1,10))
        elif siap == "3":
            main((1,100))
        elif siap == "4":
            while True:
                print("0.Kembali")
                print("Tinggal Di Tambah 1 + 1 + 1 Soal\nBerikutnya Jawaban Bertama Akan Di\nTambah Ke Soal Berikitnya")
                kembali = (input("Kembali:"))
                os.system("cls")
                if kembali == "0":
                    break
                else:
                    pass        
        elif siap == "t":
            break
        else:
            pass        
while True:
    print("0.Keluar\n1.Bermain")
    pilihan = (input("Pilihan:"))
    mulai = time.time()
    os.system("cls")
    if pilihan == "0":
        break
    elif pilihan == "1":
        persiapan()
    else:
        print(f"Tidak ada pilihan {pilihan}")