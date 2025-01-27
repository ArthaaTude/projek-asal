print("RAPOT")
while True:
    try:
        nama=(input("MASUKKAN NAMA ANDA:"))
        print("NAMA ANDA ADALAH",nama)
        rapot=int(input("NILAI RAPOT KAMU:"))
        print("NAMA ANDA:",nama)
        print("NILAI ANDA ADALAH:",rapot)
        
        if rapot < 0:
            print("GAGAL")
        elif 0 <= rapot < 60:
            print(nama,"DI BAWAH KKM ANDA DINYATAKAN TIDAK LULUS!!!")
        elif 60 <= rapot < 70:
            print(nama,"LUMAYAN",rapot)
        elif 70 <= rapot < 90:
            print(nama,"PINTAR")
        elif 90 <= rapot < 100:
            print("TERLAU PINTAR")
        break
    except ValueError:
        print("LULUS")                              