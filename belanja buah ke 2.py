nama=(input("nama:"))
while True:
    try:
        buah=(input("nama buah:"))
        if buah=="":
            print("kosong")
            continue
        elif buah in ["jus","melon","mangga"]:
            harga_buah={
                "jus":200,
                "melon":400,
                "mangga":500,
            }
        else:
            print(buah,"tidak ada!!!")
            continue
        total_harga=int(input("mau beli berapa buah:"))
        total_harga=harga_buah[buah]*total_harga
        print(nama,"harus bayar buah",buah,total_harga)
        mau=(input("y/t untuk melanjutkan:"))
        if mau=="":
            print("kosong")
            break
        elif mau=="y":
            continue
        elif mau=="t":
            break
        else:
            print("salah inputan")
            break          
    except ValueError:
        print("hanya angka!!!")    