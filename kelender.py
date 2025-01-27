import os
os.system("cls")
import calendar
selesai = True
while selesai:
    try:
        bulan = int(input("bulan:"))
        if bulan >= 13:
            os.system("cls")
            print("Tidak ada bulan",bulan)
        elif bulan <= 0:
            pass
        else:    
            while selesai:
                tahun = int(input("tahun:"))
                
                os.system("cls")
                if tahun <= 1000:
                    print("Tidak ada tahun",tahun)
                elif tahun >= 9999:
                    pass
                else:
                    os.system("cls")
                    print(calendar.month(tahun,bulan))
                    break
    except ValueError:
        print("angka")