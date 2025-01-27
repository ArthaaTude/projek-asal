selesai = True
while selesai:
    nama = (input("Masukkan Nama:"))

    if not nama.isalpha():
        print("Gagal")
    else:
        while selesai:
            pilih_hurup = (input("Masukkan Hurup:"))
            if not pilih_hurup.isalpha():
                print("Hanya Hurup")
            else:  
                tebak_hurup = (input("Tebak Hurup:"))
        
                if pilih_hurup == tebak_hurup:
                    print("Benar",nama)
                else:
                    print("Salah","Hurup Yang Di Tebak adalah",pilih_hurup)
                    selesai = False