import os
os.system("cls")
def pertama():
    def kali():
        kalii = int(input("kali:"))
        kalii *= total
        os.system("cls")
        print("Nilai sebelumnya",total)
        print("Hasil",kalii)
    def kurang():
        kurangg = int(input("kurang:"))
        kurangg -= total
        os.system("cls")
        if kurangg <= total:
            print("Nilai sebelumnya",total)
            print("Hasil",kurangg)
        else:
            print("Tidak bisa")
    def bagi():
        bagii = int(input("bagi:"))
        bagii /= total
        os.system("cls")
        if bagii <= total:
            print('Nilai sebelumnya',total)
            print("Hasil",bagii)
        else:
            print("Tidak bisa")    
    def pangkat():
        pangkatt = int(input("pangkat:"))
        pangkatt **= total
        os.system("cls")
        print("Nilai sebelumnya",total)
        print("Hasil",pangkatt)     
    selesai = True
    data = []
    while selesai:
        try:
            nomer = int(input("nomer:"))
            data.append(nomer)
            os.system("cls")
            total = sum(data)
            
            print("0 Untuk Pilihan")    
            print(f"hasil {total}")
            
            if nomer == 0:
                while selesai:
                    print("[pilihan: - * / **]")
                    pilihan = (input("pilihan:"))
                    
                    if pilihan.isdecimal():
                        print("Gagal")
                    else:
                        while selesai:
                            try:
                                if pilihan == "*":
                                    kali()
                                elif pilihan == "-":
                                    kurang()
                                elif pilihan == "/":
                                    bagi()
                                elif pilihan == "**":
                                    pangkat()
                                else:
                                    print("Pilihan Tidak ada")
                                    break
                            except ValueError:
                                print("harus angka")              
        except ValueError:
            print("harus angka")
def kedua():            
    while True:
        try:        
            pertama = int(input("pertama:"))
            kedua = int(input("kedua:"))        
            pilihan = (input("pilihan:"))

            os.system("cls")
            if pilihan == "+":
                print(pertama+kedua)
            elif pilihan == "-":
                print(pertama-kedua) 
            elif pilihan == "*":
                print(pertama*kedua)
            elif pilihan == "**":
                print(pertama**kedua)
            elif pilihan == "/":
                print(pertama/kedua)
                break
        except ZeroDivisionError:
            print("Tidak bisa")
        except ValueError:
            print("hanya angka")
print("Kalkulator")
while True:
    try:
        pilih = int(input("pilihan:"))

        if pilih == 1:
            pertama()
        elif pilih == 2:
            kedua()
        else:
            print("Tidak ada")
    except ValueError:
        print("Hanya Angka")