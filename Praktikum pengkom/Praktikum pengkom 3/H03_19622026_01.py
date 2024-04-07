# NIM/ Nama : 19622026/Muhammad Althariq Fairuz
# Tanggal : 20 oktober 2022
# Deskripsi : Menentukan harga barang dengan diskon terbesar atau menampilkan 
#             barang dengan index terkecil jika ada 2 barang dengan diskon yang sama
#KAMUS :
# barang,highestdisc,indexbarang : int
# harga,diskon,besardiskon : array of int


#ALGORITMA
barang = int(input('Masukkan jumlah barang : ')) #input jumlah barang
harga = [ 0 for i in range (barang) ]
diskon = [ 0 for i in range (barang) ]
besardiskon = [ 0 for i in range (barang) ]

for i in range (barang) :
    harga[i] = int(input(f'Masukkan harga barang ke-{i+1} : ')) #input harga barang
for i in range (barang):
    diskon [i] = int(input(f'Masukkan diskon (dalam persen) barang ke-{i+1} : ')) #input diskonnya

    besardiskon[i] = harga[i]* (diskon[i]/100) #cari besar diskon

highestidsc = 0 #deklarasikan diskon max
indexbarang=0
for i in range (barang) :
    if besardiskon[i] > highestidsc :
        highestidsc = besardiskon [i]
        indexbarang += i + 1 #agar barangnya sesuai urutan,karena ga ada barang ke 0,hanya ada index ke 0
print (f'Barang dengan diskon terbesar yaitu {indexbarang} dengan diskon {highestidsc}')












