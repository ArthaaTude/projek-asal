import random
import os
kesalahan = 0
nyawa = 3
while True:
    try:
        nomer = int(input("nomer:"))
        acak = random.randint(1,5)
        
        if nomer <= 0:
            print("tidak ada")
        elif nomer >= 6:
            print("lebih")
        else:
            os.system("cls")
            nyawa -= 1
            os.system("cls")
            if nomer <= nyawa:
                print("nyawa anda:",nyawa)
            else:
                print("Game Over")
                break
            if nomer == acak:
                print("benar")
                print("kesalahan:",kesalahan)
                break
            else:
                kesalahan += 1
    except ValueError:
        print("hanya angka")