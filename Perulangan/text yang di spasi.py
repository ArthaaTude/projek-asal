input_user = input("Masukkan teks atau angka yang ingin diulang: ")

if input_user.isdigit():
    jumlah = int(input_user)
    for i in range(jumlah):
        print(input_user)
else:
    jumlah = len(input_user)
    for i in range(jumlah):
        print(input_user[i])