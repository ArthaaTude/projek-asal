import random
while True:
    try:
        nama = (input("Nama Kamu:"))
        binatang = random.randint(1,6)
        
        if not nama.isalpha():
            print("Tidak Boleh")
        else:    
            print("Perhatikan ini di mana Kucing Berada")
            print("-__-"*6)
            print("1 Sampai 6")
            pilihan_binatang = int(input("Pilihan kamu:"))
   
            if pilihan_binatang == binatang:
                print("Selamat Kamu Menang",nama)  
            else:
                print("Maaf Kamu kalah",nama,"Ada Di Nomer:",binatang)
                if pilihan_binatang <= 6:
                    pass
                else:
                    print("Lebih",pilihan_binatang)
    except ValueError:
        print("Masukan Angka Yang Benar")