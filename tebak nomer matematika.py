import os
import random
os.system("cls")
    
def main():
    benar = 0
    total_salah = 0
    while True:
        salah = 0
        print("1.Gampang\n2.Susah")
        level = (input("Level:"))
        
        if level == "1":
            nomer_pertama = random.randint(1,10)
            nomer_kedua = random.randint(1,10)
        elif level == "2":
            nomer_pertama = random.randint(1,100)
            nomer_kedua = random.randint(1,100)
        else:
            os.system("cls")
            print(f"Pilihan Tidak ada {level}")
            continue
        oprasi = random.choice("+-x")
        
        if oprasi == "+":
            hasil = nomer_pertama + nomer_kedua
        elif oprasi == "-":
            hasil = nomer_pertama - nomer_kedua
        elif oprasi == "x":
            hasil = nomer_pertama * nomer_kedua
        elif oprasi == "/":
            hasil = nomer_pertama / nomer_kedua
        print(f"{nomer_pertama} {oprasi} ? = {hasil}")
            
        while True:
            try:
                nomer = int(input("Nomer:"))
                
                os.system("cls")
                if nomer == nomer_kedua:
                    benar += 1
                    print(f"Permainan {benar}\nTotal salah {total_salah}")
                    break
                else:
                    salah += 1
                    total_salah += 1
                    if salah >= 3:
                        if nomer == 0:
                            print(f"Permainan {benar}\nTotal salah {salah}\nSalah {salah}")
                            exit()
                        print("0.Keluar")
                    
                    elif total_salah >= 10:
                        exit()
                    print(f"Salah {salah}")
            
            except ValueError:
                os.system("cls")
            print(f"{nomer_pertama} {oprasi} ? = {hasil}")
while True:
    print("0.Keluar\n1.Mulai")
    pilihan = int(input("pilihan:"))

    os.system("cls")
    if pilihan == 0:
        break
    elif pilihan == 1:
        main()
    else:    
        pass   