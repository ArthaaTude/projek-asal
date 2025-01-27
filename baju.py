import os
os.system("cls")

def laundry():
    def baju():
        while True:
            jumlah_baju = int(input(f"jumlah {pakaian}:"))
            print(10+jumlah_baju) 
            laundry()
    print("1.untuk kembali")      
    while True:
        pakaian = (input("pakaian laundry:"))
        
        os.system("cls")
        if pakaian in ["baju","celana"]:
            if pakaian == "baju":
                baju()
            elif pakaian == "celana":
                baju()  
        elif pakaian == "1":
            break
        else:
            print("tidak ada",pakaian)        
def strika():
    print("1 untuk kembali")
    while True:
        pakaian = (input("pakaian strika:"))
        
        os.system("cls")
        if pakaian in ["suprai","bed"]:
            if pakaian == "suprai":
                print("harga",pakaian,"3.000")
            elif pakaian == "bed":
                print("harga",pakaian,"2.000")
            else:
                pass    
        elif pakaian == "1":
            break
        else:     
            print("harga",pakaian,"600")
                
while True:
    print("1.laundry\n2.strika")
    try:
        pilihan = int(input("pilihan:"))
        
        os.system("cls")
        if pilihan == 1:
            laundry()
        elif pilihan == 2:
            strika()
        else:
            print("tidak ada")
    except ValueError:
            os.system("cls")
            print("hanya angka")