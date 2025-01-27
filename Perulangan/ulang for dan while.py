for a in range(1,3):
    for b in range(1,3):
        print(a,b)

for c in range(2):
    print("perulangan luar:",c)
    for d in range(10):
        print("perulangan dalam:",d)
        if d == 1:
            break
print()

for hurup in "coding bos":
    if hurup ==" ":
        break
    print(f"kode saat ini:{hurup}")
print()

nomer = [1,2,3,4,5,6]
for f in nomer:
    if f == 6:
        print("di temukan")
        break
else:
    print("tidak di temukan")
    
print()
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

print()
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
print()
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)
print("cara ke dua")
angka = [1, 2, 3, 4]
pangkat = [z**2 for z in angka]
print(pangkat)