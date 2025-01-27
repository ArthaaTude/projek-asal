import os 

selesai = True
data = set()
print(""* 5,"data","hapus")
while selesai:
    nama = (input("nama:"))
    
    if nama.isdigit():
        print("Gagal")
    elif nama == "":
        yakin =  input("yakin keluar: Y/T:")
        if yakin == "y":
            os.system("cls")
            break
        elif yakin == "t":
            pass
        else:
            print("tidak ada")
    elif nama in data:
        print("Nama Sudah Ada")
    elif nama == "data":
        os.system("cls")
        for i,nama in enumerate(data,start=1):
            print(f"{i}.{nama}")
    elif nama == "hapus":
        while selesai:
            os.system("cls")
            for x in data:
                print(x)
            hapus = input("hapus:")
            
            if hapus == "keluar":
                break
            else:
                if hapus in data:
                    data.remove(hapus) 
    else:
        os.system("cls")
        data.add(nama)
for b,nama in enumerate(data,start=1):
    print(f"{b}.{nama}")