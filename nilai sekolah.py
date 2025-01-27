print("MATA PELAJARAN SEKOLAH")
while True:
    try:
        nama=(input("MASUKKAN NAMA ANDA:"))
        umur=int(input("MASUKKAN UMUR ANDA:"))
        sekolah=(input("MASUKKAN SEKOLAH ANDA:"))
        biologi=int(input("MASUKKAN NILAI BIOLOGI:"))
        matematika=int(input("MASUKKAN NILAI MATEMATIKA:"))
        kimia=int(input("MASUKKAN NILAI KIMIA:"))

        rata_rata=(biologi+matematika+kimia)

        if rata_rata < 0 :
            print("gagal")
        if 0 <= rata_rata < 60:
            print(nama,"ANDA TIDAK LULUS!!!")
        if 60 <= rata_rata >= 100:
            print(nama,"ANDA LULUS")
            print("ANDA MENDAPATKAN NILAI:",rata_rata)
            print("UMUR ANDA:",umur,"TAHUN","SEKOLAH ANDA:",sekolah)
        else:
            print("ANDA MENDAPATKAN NILAI:",rata_rata)
        break
    except ValueError:
        print("HANYA ANGKA")