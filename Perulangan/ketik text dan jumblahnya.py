text = input("Masukkan text: ")
nomer = int(input("Berapa kali diulang: "))

for a in range(1, nomer + 1):
    print(f"{text} {format(a,"1")}")
    
             