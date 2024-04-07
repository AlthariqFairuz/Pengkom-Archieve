# NIM/Nama : 19622026/ Muhammad Althariq Fairuz
# Tanggal : 4-11-2022
# Deskripsi : Menentukan apakah susunan benda sesuai dengan perintah tuan leo
# KAMUS
# a : int, panjang array
# M : array of int
# Fungsi pencari nilai minimum
def nilaiMin (a,M) :
    nilai = []
    for i in range (a) :
        if (nilai == [] and M[i] != 0) :
            nilai = M[i]
        if (M[i] != 0 and M[i] < nilai ) :
            nilai = M[i]
    return nilai    
# Fungsi pengurangan 
def pengurangan (nmin,a,M) :
    for i in range(a) :
        if (M[i] != 0) :
            M[i] -= nmin
    return M

# ALGORITMA
# Inpul jumlah elemen
a = int(input('Masukkan banyak nilai : '))
M = [0 for i in range (a)]

#input elemen array
for i in range (a) :
    M[i] = int(input(f'Masukkan nilai ke-{i+1} : '))

# Jalankan fungsi
print(*M)
for i in range (a) :
    x = nilaiMin(a,M)
    M = pengurangan (x,a,M)
    print (*M)






