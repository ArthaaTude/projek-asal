import os
os.system("cls")

def berurut():
    print("Dasar Perkalian\n Contoh\n 1 x 1\n 1 x 2")
    while True:
        try:
            print("0.Kembali")
            pilihan = int(input("pilihan 1 - 9:"))

            if pilihan >= 10:
                pass
            elif pilihan <= 0:
                os.system("cls")
                break
            else:
                os.system("cls")
                for __ in range(pilihan):
                    def main(data):
                        while True:
                            print("0.Ganti")
                            nomer = int(input(f"Nomer {pilihan} x :"))
                            
                            if nomer == 0:
                                os.system("cls")
                                break
                            elif nomer >= 999999:
                                print("Nomer terlalu besar")
                            else:    
                                os.system("cls")
                                for a in range(nomer + 1):
                                    for b in data:
                                        hasil = b * a
                                        print(f"{b} x {a} = {hasil}")
            main(data=[pilihan])
        except ValueError:
            os.system("cls")
            print("Angka")
def kali():
    print("Kali\nContoh\n 1 x 1\n 2 x 2")
    while True:
        try:
            print("0.kembali")
            nomer = int(input("Nomer:"))
            
            os.system("cls")
            if nomer == 0:
                break
            elif nomer >= 999999:
                print("Terlalu banyak")
            else:    
                for a in range(nomer + 1):
                    hasil = a * a
                    print(f"{a} x {a} = {hasil}")
        except ValueError:
            print("angka")

while True:
    print("0.Keluar\n1.Dasar Perkalian\n2.Kali")
    pilihan = (input("pilihan:"))
    
    os.system("cls")
    if pilihan == "1":
        berurut()
    elif pilihan == "2":
        kali()
    elif pilihan == "0":
        break    
    else:
        print("Tidak ada",pilihan)