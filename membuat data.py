import os
import pandas as pd

os.system("cls")

tambah = []
data = int(input("Jumlah Data:"))
for a in range(1,data + 1):
    nama = str(input(f"Data {a} = "))
    
    tambah.append(nama)
os.system("cls")

df = pd.DataFrame({
    "nama":tambah
})

while True:
    print(df)
    ingin = input("Hapus Data Y/T?:")

    os.system("cls")
    if ingin == "y":
        break
    elif ingin == "t":
        print(df)
        exit()
    else:
        print(f"Tidak Sesuai {ingin}")
print(df)

while True:
    try:
        nomer = int(input("Nomer di hapus:"))
        if nomer >= data:
            os.system("cls")
            print(f"{nomer} Lebih dari data yang ada")
            print(df)
        else:
            os.system("cls")
            print(df.drop(index=nomer))
            break
    except ValueError:
        print("Hanya Angka")