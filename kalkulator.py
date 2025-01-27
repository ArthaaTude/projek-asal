print("kalkulator")
while True:
    try:
        pertama=int(input("MASUKKAN ANGKA PERTAMA:"))
        kedua=int(input("MASUKKAN ANGKA KEDUA:"))
        bebas=(input("MASUKKAN + * / -:"))

        if bebas=="+":
            print(pertama,"+",kedua,"=",pertama+kedua)
        elif bebas=="-":
            print(pertama,"-",kedua,"=",pertama-kedua)
        elif bebas=="*":
            print(pertama,"x",kedua,"=",pertama*kedua)     
        elif bebas=="/":
            print(pertama,":",kedua,"=",pertama/kedua) 
        else:
            print("HANYA + * / -")
            break
    except ValueError:
        print("HANYA ANGKA!!!")