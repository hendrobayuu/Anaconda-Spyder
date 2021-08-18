#nama file.csv
#D:Python
import csv
#lokasi file, nama file, dan inisialisasi csv
f = open ('nama file.csv', 'r')
reader = csv.reader(f)
#membaca baris per baris
for row in reader:
    print(row)
# menutup file csv
f.close()
