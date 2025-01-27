import os
import random
os.system("cls")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

text = ["Macan Kumbang","Macan putih","Macan loreng","Singa putih",
        "Hanoman","Buaya putih","Buaya putih","serigala putih","Naga sastro",
        "Kera sakti","Naga barong","Naga emas","Sangrilagita","kosong"]

kodam_index = 0
kodam_list = text.copy()
random.shuffle(kodam_list)
data = []
data_kodam = []
jumlah_data = 0

while True:
    cek_kodam = (input("Cek Kodam Y/T:"))
    clear()
    if cek_kodam == "y":
        
        while True:
            if kodam_index >= len(kodam_list):
                random.shuffle(kodam_list)
                kodam_index = 0
            kodam = kodam_list[kodam_index]
            kodam_index += 1
            nama = (input("nama:")).capitalize()
            
            clear()
            if nama == "0":
                exit()
            elif nama == "1":
                data.clear()
                jumlah_data = 0
            elif nama == "2":
                print("INI CUMA BERCANDA SAJA!!!")
                for a,lihat in enumerate(data):
                    print(f"{lihat} Kodam :{data_kodam[a]}")
            elif not nama.replace(" ","").isalpha():
                print("Gagal")
            elif len(nama) >= 10:
                panjang = len(nama)
                print(f"Terlalu Panjang {panjang} !!!")
            elif len(nama) <= 2:
                pendek = len(nama)
                print(f"Nama Terlalu Pendek {pendek} !!!")     
            else:
                data.append(nama)
                data_kodam.append(kodam)
                jumlah_data += 1
                for i,item in enumerate(data):
                    print(f"{item} Kodam: {data_kodam[i]}")
                print()    
                print("="*10,"0.keluar","="*10)
                print("="*10,"1.Riset Data","="*10)
                print("="*10,"2.Lihat Data","="*10)
                print("="*10,"Jumlah Data:",jumlah_data,"="*10)
    elif cek_kodam == "t":
        break
    else:
        pass