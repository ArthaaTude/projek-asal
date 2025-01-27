while True:
    nama=(input("NAMA:"))
    if "," in nama or "." in nama:
        print(nama,"TIDAK BOLEH ,.")
    elif nama=="":
        print("TIDAK BOLEH KOSONG!!!")
    else:
        break
while True:
    try:
        umur=int(input("UMUR:"))
        break
    except ValueError:
        print("HANYA ANGKA!!!")
sekolah=(input("SEKOLAH:"))
kelas=(input("KELAS:"))

print()
print("==========================DATA===============================")
if umur <= 0:
    print(umur,"GAGAL")
elif umur <= 15:
    print("TERLALU BOCIL",umur)
elif umur <= 100:
    print("UMUR ANDA ADALAH:",umur,"BERHASIL!!!")
    if "," in sekolah or "." in sekolah:
        print(sekolah,"TIDAK BOLEH PAKEK ,.")
else:
    print("TERLALU MELEBIHI BATAS UMUR!!!")

print("NAMA ANDA:",nama)
print("NAMA KELAS:",kelas)
print("NAMA SEKOLAH:",sekolah)