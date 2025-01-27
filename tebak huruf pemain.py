import random
kesalahan = 0
while True:
    hurup = (input("Masukkan Huruf:").upper())
    tes = "abcdef"
    acak = random.choice(tes).upper()
    
    if len(hurup) == 2 and hurup.isalpha():
        print("Gagal")
    else:
        if hurup == acak:
            print("Benar")
            print("Kesalahan Anda",kesalahan)
            break
        else:
            kesalahan += 1
            print("Yang Benar",acak)