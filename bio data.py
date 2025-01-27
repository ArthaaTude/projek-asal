def validasi_angka(intejer):
    try:
        int(intejer)
        return True
    except ValueError:
        return False

print("BIO DATA SAYA!!!")
try:
    nama=(input("MASUKKAN NAMA:"))
    kelas=int(input("MASUKKAN KELAS:"))
    asal=(input("MASUKKAN ASAL:"))
    umur=int(input("MASUKKA UMUR:"))
    
    if validasi_angka(umur):
        umur=int(umur)
    else:
        raise ValueError("UMUR HARUS BERUPA ANGKA!!!")
    print("===================DATA=====================")
    print("NAMA ANDA ADALAH:",nama)
    print("KELAS ANDA:",kelas)
    print("ASAL ANDA:",asal)
    print("UMUR ANDA:",umur)
    print("============================================")
except ValueError:
    print("GAGAL")