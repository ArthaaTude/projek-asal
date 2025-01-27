import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error

def main():
    os.system("cls")

    x = np.arange(100 , 210).reshape(-1,1) # tinggi fitur
    y = np.arange(20,130) # berat target

    model = LinearRegression()
    model.fit(x,y)

    tinggi = int(input("Tinggi:"))
    
    if tinggi >= 250 or tinggi <= 0:
        main()
    else:    
        data_baru = model.predict([[tinggi]])
        prediksi = model.predict(x)

        os.system("cls")
        score = r2_score(y,prediksi)
        error_absolute = mean_absolute_error(y,prediksi)
        error_squared = mean_squared_error(y,prediksi)
        cek_squared = np.sqrt(error_squared)
        cek_absolute = np.sqrt(error_absolute)
        print(f"Error Absolute: {cek_absolute}\nError Squared: {cek_squared}")
        print(f"Score {score}\nTinggi {tinggi} Berat {data_baru[0]}")

        ingin = (input("Ingin Menampilkan Data Y/T:"))

        if ingin == "y":
            plt.scatter(x,y,color="blue",label="Asli")
            plt.plot(x,y,color="red",label="garis lulus")
            plt.xlabel("Tinggi")
            plt.ylabel("Berat")
            plt.legend()
            plt.show()
        else:
            pass
main()

while True:
    ulang = input("Ulang Y/T:")

    if ulang == "y":
        main()
    elif ulang == "t":
        break    
    else:
        pass