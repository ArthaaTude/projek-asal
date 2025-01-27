angka = [10,5,2,7,3,8,9,6,4,1]

for i in range(len(angka)-1):
    for  j in range(len(angka)-i-1):
        if angka[j]>angka[j+1]:
            angka[j],angka[j+1]=angka[j+1],angka[j]
print(angka)            

# Baris pertama, angka = [10, 5, 2, 7, 3, 8, 9, 6]:, 
# mendefinisikan daftar angka dengan nilai-nilai 10, 5, 2, 7, 3, 8, 9, dan 6.
# Baris kedua, for i in range(len(angka) - 1):, membuat loop for 
# yang akan mengulangi kode di dalam bloknya sebanyak len(angka) - 1 kali.
# Baris ketiga hingga kelima, for j in range(len(angka) - i - 1):, membuat loop for 
# yang akan mengulangi kode di dalam bloknya sebanyak len(angka) - i - 1 kali.
# Baris keenam, if angka[j] > angka[j + 1]:, memeriksa apakah nilai elemen angka 
# pada indeks j lebih besar dari nilai elemen angka pada indeks j + 1.
# Jika ya, maka baris ketujuh, angka[j], angka[j + 1] = angka[j + 1], angka[j]:, 
# akan menukar nilai kedua elemen tersebut