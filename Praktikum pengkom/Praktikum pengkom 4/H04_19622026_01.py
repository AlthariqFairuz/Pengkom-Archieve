# NIM/Nama : 19622026/ Muhammad Althariq Fairuz
# Tanggal : 4-11-2022
# Deskripsi : Menentukan apakah susunan benda sesuai dengan perintah tuan leo (Benda paling berat dalam satu tumpukkan ahrus paling bawah)
# KAMUS
# tinggi,banyak,sesuai = int, 
# matrixbenda = matrix of int
# ALGORITMA
tinggi = int(input('Masukkan Tinggi tumpukan : '))
banyak = int(input('Masukkan Banyak tumpukan : '))
matrixbenda = [[0 for i in range(banyak)] for j in range (tinggi)]
for i in range (tinggi) :
    for j in range (banyak) :
        matrixbenda [i][j] = int(input(f'Masukkan benda pada baris ke-{i+1} kolom ke-{j+1} :'))

#Cek kesesuaiannya,yaitu dengan mencek apakah benda yang paling berat benar2 diletakkan di paling bawah
sesuai = 0
for i in range (tinggi-2,-1,-1) :
    for j in range (banyak) :
        if matrixbenda[tinggi-1][j] >= matrixbenda [i][j]:
            sesuai += 1
#Jika benar diletakkan paling bawah,harusnya nilai 'sesuai' sama dengan (tinggi-1) x banyak,tinggi dikurangi 1 karena kita menjadikan tumpukkan terakhir sebagai patokan/yang diujikan gitu 
if sesuai == ((tinggi-1)*banyak) :
    print ("Susunan tersebut memenuhi perintah tuan leo.")
else :
    print ('Susunan tersebut tidak emmenuhi perintah tuan leo.')

