import os
import pandas as pd

os.system("cls")

data = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'John', 'Tom', 'John',"Di Hapus"],
    'Age': [20, 21, 19, 20, 18,9],
})

x = data.drop(index=5)
print(x)