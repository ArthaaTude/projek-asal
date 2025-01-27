print("KATA TIDAK BOLEH PAKEK SIMBOL!!!")
selesai=False
while not selesai:
    while True:
        tinggal=(input("Tinggal Dimana:"))
        if not tinggal.isalpha():
            print("tidak boleh")
            selesai=False
            continue
        else:
            break    
    nama=(input("Nama Anda:"))
    if not nama.isalpha():
        print("Tidak Boleh")
        continue
    while not selesai:
        try:    
            nama_bapak=(input("Nama Bapak:"))
            if not nama_bapak .isalpha():
                print("Tidak Boleh")
                continue
            while True:
                umur_bapak=int(input("Umur Bapak:"))
                if umur_bapak <= 0:
                    print(umur_bapak,"Tidak Boleh")
                elif umur_bapak <= 1000:
                    break
                else:
                    print(umur_bapak,"Melebihi 1000")
        except ValueError:
            print("Hanya Angka!!!")
            continue
        while not selesai:
            try:
                nama_ibuk=(input("Nama Ibuk:"))
                if not nama_ibuk.isalpha():
                    print("Tidak Boleh")
                    continue
                while True:
                    umur_ibuk=int(input("Umur Ibuk:"))
                    if umur_ibuk <= 0:
                        print(umur_ibuk,"Tidak Ada!!!")
                    elif umur_ibuk <= 1000:
                        break
                    else:
                        print(umur_ibuk,"Melebihi Batas")
                        continue
            except ValueError:
                print("Hanya Angka")
                continue         
            while not selesai:
                nama_nenek=(input("Nama Nenek:"))
                if not nama_nenek.isalpha():
                    print("Tidak Boleh")
                    continue
                while True:
                    try:
                        umur_nenek=int(input("Umur Nenek:"))
                        if umur_nenek <= 0:
                            print(umur_nenek,"Tidak Ada")
                        elif umur_nenek <= 1000:
                            break
                        else:
                            print(umur_nenek,"Melebihi 1000")
                            continue
                    except ValueError:
                        print("Hanya Angka")
                        continue    
                while not selesai:
                    nama_kakek=(input("Nama Kakek:"))
                    if not nama_kakek.isalpha():
                        print("Tidak Boleh")
                        continue
                    while True:
                        try:
                            umur_kakek=int(input("Umur Kakek:"))
                            if umur_kakek <= 0:
                                print(umur_kakek,"Tidak Ada")
                            elif umur_kakek <= 1000:
                                break
                            else:
                                print(umur_kakek,"Melebihi Batas")
                                continue
                        except ValueError:
                            print("Hanya Angka")
                            continue    
                    while not selesai:
                        try:
                            umur_anda=int(input("Umur Anda:"))
                            if umur_anda <= 0:
                                print(umur_anda,"Tidak Ada!!!")
                            elif umur_anda <= 1000:
                                selesai=True
                            else:
                                print(umur_anda,"Melebihi 1000")    
                        except  ValueError:
                            print("Hanya Angka!!!")        
print("=========================Data===============================")                        
print("Nama Anda:",nama)                                              
print("Nama Bapak:",nama_bapak)                        
print("Nama Ibuk:",nama_ibuk)                        
print("Nama Nenek:",nama_nenek)                        
print("Nama Kakek:",nama_kakek)
print("Tinggal Di:",tinggal)
print("=========================Umur===============================")                        
print("Umur:",nama_bapak,":",umur_bapak)                        
print("Umur:",nama_ibuk,":",umur_ibuk)                        
print("Umur:",nama_kakek,":",umur_kakek)                        
print("Umur:",nama_nenek,":",umur_nenek)               