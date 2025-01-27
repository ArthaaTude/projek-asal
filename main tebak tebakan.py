import random
kesalahan = 0
while True:
    try:
        tebak_nomer = int(input("nomer:"))
        nomer_acak = random.randint(0,3)
        if len(str(tebak_nomer)) != 1:
            print("gagal")
        else:
            if tebak_nomer == nomer_acak:
                print("benar")
                print("kesalahan anda",kesalahan)
                break
            else:
                kesalahan += 1
                print("salah berada di nomer:",nomer_acak)  
    except ValueError:
        print("hanya angka")
kesalahan_hurup = 0        
while True:
    tebak_huruf =  (input("huruf:").upper())
    hurup_acak = "abcdef"
    hasil = random.choice(hurup_acak).upper()
    if tebak_huruf  == hasil:
        print("benar")
        print("kesalahan anda",kesalahan_hurup)   
        break
    elif len(tebak_huruf) == 2 and tebak_huruf.isalnum():
        print("gagal")
    else:
        kesalahan_hurup += 1
        print("salah",hasil)