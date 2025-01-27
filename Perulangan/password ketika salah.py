# untuk menyimpan password
password = ""

# perulangan dengan while dan membuat password
while password != "a":
    # memasukkan password
    password = input("Masukkan Password : ")
    # mengetahui password salah
    try:
        # membuat percabangan 
        if password != "a":
            # password salah
            raise ValueError(password,"salah")
    except ValueError as ahsiap:
        print(ahsiap)
# password benar
print(password,"benar")        