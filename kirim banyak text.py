while True:
    try:
        nama=(input("nama:"))
        
        if "," in nama or "." in nama:
            print(nama,"tidak boleh ,.")
            continue
        elif nama=="":
            print("kosong")
            continue
        umur=int(input("umur:"))
        
        if umur <= 0:
            print(umur,"tidak ada!!!")
        elif 1 <= umur <= 100:
            break
        else:
            print("tidak ada:")
            break
    except ValueError:
        print("angka")
print("=========data===========")        
print("nama:",nama)                
print("umur:",umur)

text=(input("text:"))
nomer=int(input("berapa text yang akan terkirim:")) 

print() 
for a in range(1, nomer  +1):
    print(nama,text)                  