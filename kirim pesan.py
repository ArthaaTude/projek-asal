while True:
    nama=(input("NAMA:"))
    if "," in nama or "." in nama:
        print("TIDAK BOLEH ,.")
        continue
    elif nama=="":
        print("KOSONG")   
        continue
    break
while True:
    text=(input("TEXT:"))
    # Kondisi ini akan memeriksa apakah teks yang dimasukkan berupa huruf alfabet. Jika bukan, maka akan menampilkan output "GAGAL".
    if not text.isalpha():
        print("GAGAL")
    elif text=="":
        print("KOSONG")
        continue
    else:
        print("UNTUK KAMU",nama,"I LOVE YOU")
        break
while True:                
    try:
        nomer=int(input("BERAPA PESAN TEXT:"))
        break
    except ValueError:
        print("HANYA ANGKA!!!")
for a in range(1,nomer +1):
    print(text,a)