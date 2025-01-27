membuat_bintang = int(input("nomer bintang:"))

for a in range(1,membuat_bintang +1):
    for b in range(a+1):
        print("*",end="")
    print()    