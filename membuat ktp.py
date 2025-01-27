sesuai = True
while sesuai:
    nama = (input("nama:"))
    
    panjang = len(nama)
    print("jumblah nama anda:",panjang)
    if len(nama) >= 20:
        print("lebih")
    elif nama.isdigit():
        print("salah input")
    else:
        while sesuai:  
            try:
                umur = int(input("umur:"))
                if umur <= 0:
                    print("tidak ada")
                elif umur <= 17:
                    print("gak bisa")
                elif umur <= 1000:
                    while sesuai:
                        sekolah = (input("sekolah:"))
                        if sekolah.isdigit():
                            print("gagal")
                        else:
                             while sesuai:
                                 bapak = (input("bapak:"))
                                 ibuk = (input("ibuk:"))
                                 sesuai = False
                                 print("=======Data========")
                                 print("nama:",nama)
                                 print("umur:",umur)
                                 print("sekolah:",sekolah)
                                 print("ibuk:",ibuk)
                                 print("bapak:",bapak)
                else:
                    print("lebih")
            except ValueError:
                print("hanya angka")