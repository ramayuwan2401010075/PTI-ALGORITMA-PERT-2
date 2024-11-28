"""
aplikasi hitung Luas Segitiga
input: nilai Alas dan Tinggi
output: Nilai Luas Segitiga
dibuat oleh: Rama Yuwan
tgl buat: 2024-11-28
"""

#membuat salam pembuka
print("Aplikasi Hitung Luas Segitiga")

#Input Nilai Alas
alas= input ("Nilai Alas: ")

#Input Nilai Tinggi
tinggi= input ("Nilai Tinggi: ")

#proses
luas= float(alas) * float(tinggi) *0.5
txluas= "Luasnya: " + str(luas)

#output
print(txluas)
