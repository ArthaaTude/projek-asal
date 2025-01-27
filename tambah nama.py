mulai = True
while mulai:
    nama = (input("nama:"))
    
    if not nama.isalpha():
        print("gagal")
    elif len(nama) >= 8:
        panjang = len(nama)
        print("jumblah nama anda:",panjang)
        print("lebih")
    else:
        while mulai:
            pilihan = (input("ingin nambah nama: Y/T:"))
            
            if pilihan == "y":
                nama_kedua = (input("nama kedua:"))
                
                if not nama.isalpha():
                    print("gagal")
                elif len(nama_kedua) >= 8:
                    panjangg = len(nama_kedua)
                    print("jumblah nama anda",panjangg)
                    print("lebih")    
            elif pilihan == "t":
                print("tidak menambah nama")
                print("nama anda",nama)
                mulai = False
                break
            while pilihan != "y" and pilihan != "t":
                pilihan = (input("Y/T:"))
            
            if nama_kedua:
                print("nama anda",nama,"",nama_kedua)
                mulai = False
                break