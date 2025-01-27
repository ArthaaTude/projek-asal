password = ""

while password != "user":
    password = input("passoword:")
    try:
        if password != "user":
            raise ValueError("salah")
    except ValueError as a:
        print(a)
while True:        
    nama=input("nama:")
    if not nama.isalpha():
        print("nama ada simbol,spasi dan angka")
    else:    
        while True:
            try:
                umur=int(input("umur:"))
                if umur <= 0:
                    print(umur,"tidak ada")
                elif umur <= 17:
                    print("gagal")
                    break
                elif umur <= 1000:
                    hobi=(input("hobi:"))
                    if not hobi.isalpha():
                        print("nama ada simbol,spasi dan angka")
                    else:
                        break    
                else:
                    print("melebihi",umur)
                    break
            except ValueError:
                print(" hanya angka")
                                