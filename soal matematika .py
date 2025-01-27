import random
import os

def main(kesulitan,selesai = True):
    permainan = 0
    while selesai:
        pertama = random.randint(1,10 if kesulitan == "gampang" else 100)
        kedua = random.randint(1,10 if kesulitan == "gampang" else 100)
        kesalahan = 0
        kekalahan = 6
        if kesulitan == "sangat sulit":
            pertama = random.randint(100,1000)
            kedua = random.randint(100,1000)
    
        while selesai:
            print(pertama,"+",kedua)
            try:
                jawab = int(input("jawab:"))
                
                hasil = (pertama+kedua)
                
                os.system("cls")
                if jawab == hasil:
                    print("benar")
                    print("kesalahan anda",kesalahan)
                    permainan += 1
                    break
                else:
                    kekalahan -= 1
                    kesalahan += 1
                    print("Salah")
                    if jawab > kekalahan:
                        print("0 Untuk Menyerah")
                        if jawab == 0:    
                            print(pertama,"+",kedua,"=",pertama+kedua)
                            print("kesalahan anda",kesalahan)
                            print("Permainan anda",permainan)
                            selesai = False
            except ValueError:
                print("Angka")

while True:
    print("1.Susah")
    print("2.Gampang")
    print("3.Sangat Susah")
    try:
        pilihan = int(input("pilihan:"))

        if pilihan == 1:
            main("sulit")
        elif pilihan == 2:
            main("gampang")
        elif pilihan == 3:
            main("sangat sulit")    
        else:
            print("tidak ada pilihan")
    except ValueError:
        print("Angka")