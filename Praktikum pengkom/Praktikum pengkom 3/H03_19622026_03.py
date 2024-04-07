# NIM/ Nama : 19622026/Muhammad Althariq Fairuz
# Tanggal : 20 oktober 2022
# Deskripsi : Menentukan banyak substring dalam string

# KAMUS
# panjang1, panjang2,konstanta,count: int
# kata1, kata2 : string

# ALGORITMA
panjang1 = int(input(" Masukkan panjang string pertama: "))
kata1 = input(" Masukkan string pertama: ")
panjang2 = int(input(" Masukkan panjang string kedua : "))
kata2 = input(" Masukkan string kedua: ")
count = 0

for i in range(panjang2):
    if kata2[i] == kata1[0]:
        konstanta = i
        cek = 0 #untuk mencek panjang string yang sama
        for j in range(panjang1):
            if konstanta < panjang2:
                if kata2[konstanta] == kata1[j]: #kita looping 2x biar kata2nya benar2 sama,ga sekedar sama huruf aja
                    cek += 1
                konstanta += 1
        if cek == panjang1:
            count += 1 #jika panjang string yang dicek sama,maka hitungan kata yang sama bertambah 1
print(f"String pertama muncul sebanyak {count} kali")


