# NIM/Nama : 19622026/Muhammad Althariq Fairuz
# Tanggal 5-10-2022
# Deskripsi : Mencari bilangan sempurna

#Kamus
#x : int

#ALGORITMA
x= int(input('Masukkan Bilangan : '))
jmlh = 0
for i in range (1,x) :
    if x % i == 0: #dicari apakah i dalam interval 1 sampai x-1 ada faktornya atau engga
        jmlh += i
if (jmlh == x ): #jika jumlah faktornya = bilangan awal,maka memenuhi kriteria
    print (f'{x} adalah bilangan sempurna.')
else :
    print (f'{x} bukan bilangan sempurna.')



