import numpy as np
import matplotlib.pyplot as plt

# Distribusi noise
noise = np.random.normal(10, 20, size=(91,))
# Distribusi linear
x = np.arange(10,100 + 1)

# Plot histogram noise
plt.hist(noise,bins=5,edgecolor="black",color="red")
plt.title("Distribusi Noise Acak Jelek")
plt.xlabel("Nilai Noise")
plt.ylabel("Frekuensi")
plt.legend()
plt.show()

# plot linear
plt.scatter(x,x,color="blue",label="Data Linear")
plt.plot(x,x,color="red",label="Garis Linear")
plt.title("Data Linear Berurutan Bagus")
plt.legend()
plt.show()