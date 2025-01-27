import random
kesalahan = 0
makanan_salah = 0
ganti = True
artis = {
    "christy":"coklat",
    "marsha":"japota",
    "freya":"dadar gulung",
}
kata = {
    "marsha":"seperti pizza yang selalu di nanti nanti semua orang selalu nantikan aku ya",
    "freya":"terangi hari mu dengan senyuman karamel ku",
    "christy":"peduli dan berbaik hati siapa dia",
}
while ganti:
    tebak_nama = (input("Nama Artis:"))
    acak = random.choice(list(artis))
    makanan_artis = artis[acak]
    kata_kata = kata[acak]
    if not tebak_nama.isalpha():
        print("Salah Inputan")
    else:
       if tebak_nama == acak:
            print("Benar")
            print("Kesalahan Anda:",kesalahan)
            while ganti:
                tebak_makanan = (input(f"Makanan {acak} Adalah:"))
            
                if not tebak_makanan.isalpha():
                    print("Salah Inputan")
                else:
                    if tebak_makanan == makanan_artis:
                        print("Benar")
                        print("Kesalahan Anda:",makanan_salah)
                        while ganti:
                            tebak_kata = (input(f"Kata {acak} Adalah:"))
                            if tebak_kata.isdigit():
                                print("Salah Input")
                            else:
                                if tebak_kata == kata_kata:
                                    print("Benar")
                                    panjang = len(tebak_kata)
                                    print("Kata Nya Adalah",panjang)
                                    ganti = False
                                    break
                                else:
                                    print("Bukan Itu Katanya:")    
                    else:
                        makanan_salah += 1
                        print("Maaf Bukan Itu")
       else:
           kesalahan += 1
           print("Bukan Dia")       