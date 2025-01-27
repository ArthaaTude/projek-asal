print("===================PINJEM BUKU======================")
while True:
    nama=(input("NAMA:"))
    
    if "," in nama or "." in nama:
        print(nama,"TIDAK BOLEH .,")
    elif nama=="":
        print("NAMA TIDAK BOLEH KOSONG!!!")    
    else:
        break        
while True:
    try:
        umur=int(input("UMUR:"))
        if umur <= 0:
            print(umur,"GAGAL")
        elif umur < 15:
            print(umur,"MASIH BOCIL")
            continue
        elif umur <= 100:
            print
        else:
            print("MELEBIHI BATAS!!!")        
        break
    except ValueError:
        print("HANYA ANGKA!!!")
buku=(input("BUKU:"))
total_buku=int(input("TOTAL BUKU:"))

if buku in ["html","css","javascript",""]:         
    harga_buku={
        "html":100,
        "css":200,
        "javascript":300,
        "":000,
    }
    total_buku = harga_buku[buku]*total_buku
    print(total_buku,"rb",nama,"HARUS BAYAR!!!","buku",buku)    
else:
    print("TIDAK ADA!!!")       
kelas=(input("KELAS:"))
while True:
    try:
        nim=int(input("NIM:"))
        break
    except ValueError:
        print("HANYA ANGKA!!!")
print()        
print("==================DATA==================")        
print("NAMA ANDA:",nama)               
print("YANG ANDA PINJAM:","buku",buku)
print("KELAS ANDA:",kelas)
print("TOTAL BAYAR:",nama,total_buku,"rb")
print("NIM ANDA:",nim)