import os
lis = set()
def pertama():
    while True:
            global lis
            nama = (input("Nama:"))
            
            if nama.isdigit():
                print("Gagal")
            elif nama == "":
                break
            else:
                lis.add(nama)
            os.system("cls") 
            print("="*10,"Data","="*10)
            for a in lis:
                print(a)
def kedua():
    lis.clear()
    nomer = int(input("Nomer:"))
    
    for a in range(nomer):
        nama = (input(f"Nama Ke-{a+1}:"))
        
        if nama.isdigit():
            print("Gagal")
        elif nama is lis:
            print("Nama Sudah Ada")
        else:
            lis.add(nama)
    os.system("cls")
    print("="*10,"Data","="*10)           
    for b in lis:
        print(b)
print("1.Cara Pertama\n2.Cara Kedua")        
while True:
    try:
        pilihan = int(input("nomer:"))
        if pilihan == 1:
            os.system("cls")
            pertama()
            break
        elif pilihan == 2:
            os.system("cls")
            kedua()
            break
        else:
            print("Tidak ada")
    except ValueError:
        print("Hanya Angka")