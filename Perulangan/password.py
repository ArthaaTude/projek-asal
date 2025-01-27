password = ""

while password != "rahasia":
    password = input("Masukkan password:")
    try:
        if password != "rahasia":
            raise ValueError("Password salah!")
    except ValueError as a:
        print(a)
print("passord benar")    