# NIM/Nama : 19622026/ Muhammad Althariq Fairuz
# Tanggal : 4-11-2022
# Deskripsi : Menenetukan ukuran foto yang pas berdasarkan tinggi bangunan
# KAMUS
# besar: int ,ukuran matrix
# T : matrix of int , untuk nyimpan data ketinggian 
# data : matrix of int , untuk nyimpan data tertinggi dari bagian atas dan bawah
# tertinggi : int, ukuran terbaik untuk difoto
# ALGORITMA
besar = int(input("Masukkan besar Kota Kompeng: "))
# Deklarasi Matrix
T = [[0 for i in range(besar)] for j in range(besar)]
# Input Elemen Matrix
for i in range(besar):
    for j in range(besar):
        T[i][j] = int(input(f"Masukkan tinggi bangunan baris {i+1} kolom {j+1}: "))

# Cari foto bangunan tertinggi dan simpan di matrix data
data = [[0 for kolom in range(besar)] for baris in range(2)] # batesin barisnya sampai 2,untuk bagian atas dan bawah
# Cek bagian atas
for kolom in range(besar):
    for baris in range(besar):
        if (baris == 0):
            data[0][kolom] += T[baris][kolom]
            tertinggi = T[baris][kolom]
        else:
            if T[baris][kolom] > tertinggi:
                tertinggi = T[baris][kolom]
                data[0][kolom] += T[baris][kolom]
# Cek bagian bawah
for kolom in range(besar):
    for baris in range(besar-1,-1,-1):
        if (baris == besar-1):
            data[1][kolom] += T[baris][kolom]
            tertinggi = T[baris][kolom]
        else:
            if T[baris][kolom] > tertinggi:
                tertinggi = T[baris][kolom]
                data[1][kolom] += T[baris][kolom]

# Cari titik tertinggi dari data di matrix data
tertinggi = data[0][0]
for baris in range(2):
    for kolom in range(besar):
        if (data[baris][kolom] > tertinggi):
            tertinggi = data[baris][kolom]
print("Foto terbaik memiliki total tinggi :", tertinggi)