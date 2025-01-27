import os
import hashlib
os.system("cls")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def Sandi():
    while True:
        print("0.Kembali")
        sandi = input("Sandi:")
        
        clear_screen()
        if sandi == "0":
            break
        elif len(sandi) >= 16:
            asli = sandi
            encrypted_sandi = hash_password(sandi)
            data.append(("Sandi enkripsi", encrypted_sandi))
            data.append(("Sandi asli", asli))
            Cocok(sandi)
            break
        elif len(sandi) <= 8:
            hasil = len(sandi)
            print("Sandi Terlalu pendek", hasil)
        else:
            pass

def Nomer():
    while True:
        print("0.Kembali")
        try:
            nomer = int(input("Nomer:"))
            
            clear_screen()
            if nomer == 0:
                break
            elif nomer >= 18:
                data.append(("Nomer", nomer))
                Cocok(nomer)
                break
            elif nomer >= 8:
                print(f"Terlalu pendek {nomer}")
            else:
                pass
        except ValueError as e:
            print(f"Tipe kesalahan: {e}")

def Cocok(nilai):
    while True:
        cocok = input("Konfirmasi:")
        
        clear_screen()
        if cocok == str(nilai):
            clear_screen()
            print("Berhasil dibuat")
            Ganti()
            break
        else:
            print("Tidak sama")

def Ganti():
    print("1. Kembali\n2. Selesai")
    while True:
        ganti = input("Ganti:")
        
        if ganti == "2":
            clear_screen()
            for tipe, a in data:
                print(f"{tipe}: {a}")
            exit()
        elif ganti == "1":
            break
        else:
            pass
    
data = []
while True:
    print("1.Sandi\n2.Nomer")          
    pilih = input("pilihan:")
    
    clear_screen()
    if pilih == "1":
        Sandi()
    elif pilih == "2":
        Nomer()
    else:     
        print("Tidak ada")