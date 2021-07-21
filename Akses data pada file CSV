#Membaca file dengan menggunakan pandas
#NAMA FILE.csv
#D:\Python
import pandas as pd
csv_data=pd.read_csv("NAMA FILE.csv")
print(csv_data)

#Membaca file dengan menggunakan head()
#print(csv_data.head())

#melakukan akses data kolom
print(csv_data.columns)
print(csv_data['KOLOM'])

#Melakukan akses data melalui baris
print(csv_data.iloc[5]) #baris ke 5

#Menampilkan suatu data dari baris dan kolom
print(csv_data['KOLOM'].iloc[1])
print("Cuplikan Dataset: ")
print(csv_data.head())

#Menampilkan data dalam range tertentu
print("Data ke 5 - 9 dalam satu baris: ")
print(csv_data.iloc[5:10])

#Menampilkan informasi statistik dengan Numpy
print(csv_data.describe(exclude=['O']))	
#print(csv_data.describe(include='all'))
