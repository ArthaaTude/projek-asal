while True:
    try:
        nama=(input("MASUKKAN NAMA ANDA:"))
        umur=int(input("MASUKKAN UMUR ANDA:"))
        tempat_tinggal=(input("DARI MANA:"))
        buah=(input("MASUKKAN NAMA BUAH ANDA:"))
        
        if buah=="":
            print("ANDA TIDAK MEMASUKAN APA APA!!!")
        elif buah in ["apel","lemon","alpokat"]:
            print(buah,"HARGA 10RB")
            beli=int(input(f"MAU BELI BERAPA {buah.upper()}:"))
            total=beli+10
            print(f"HARGA BUAH {buah.upper()}:{beli}{total}")
        else:    
            print("TIDAK ADA") 
        lanjut=(input("APAKAH INGIN LANJUT? (YA/TIDAK):")).lower()
        if lanjut =="ya":
            print 
        else: 
            print("gagal")                  
            break
    except ValueError:
        print("HANYA ANGKA")