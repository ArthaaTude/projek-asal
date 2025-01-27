while True:
    nama=(input("nama:"))
    
    if "," in nama or "." in nama:
        print(nama,"nama tidak boleh ,.")
    elif nama=="":
        print(nama,"kosong")    
    hobi=(input("hobi:"))
    if "," in hobi or "." in hobi:
        print(hobi,"hobi tidak boleh ,.")
        break
    elif hobi=="":
        print("tidak boleh kosong!!!")
    else:             
        break
while True:
    try:
        umur=int(input("umur:"))
        
        if umur <= 0:
            print(umur,"tidak ada")
        elif 1 <= umur <= 100:
            break
        else:
            print("melebihi")    
    except ValueError:
        print("hanya angka!!!")
        break         
print("tahun kelahiran")
while True:
    try:
        tahun=int(input("tahun 1000-9999:"))
        if tahun <= 0:
            print(tahun,"tidak ada!!!")
        elif 1000 <= tahun <= 9999:
            tanggal=int(input("tanggal 1-31:"))
            if tanggal <= 0:
                print(tanggal,"tidak ada!!!")
            elif 1 <= tanggal <= 31:
                bulan=int(input("bulan 1-12:"))
                if bulan <= 0:
                    print("tidak ada!!!")
                elif 1 <= bulan <= 12:
                    print("anda berhasil")
                    break
                else:
                    print(bulan,"bulan melebihi")           
            else:
                print(tanggal,"tanggal melebihi")    
            break    
        else:
            print(tahun,"kurang")
    except ValueError:
        print("hanya angka!!!")
print()        
print("==================DATA=========================")        
print("nama:",nama)               
print("hobi:",hobi)               
print("umur:",umur)               
print("tahun:",tahun)               
print("tanggal:",tanggal)               
print("bulan:",bulan)               