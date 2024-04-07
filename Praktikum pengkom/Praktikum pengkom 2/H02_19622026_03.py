# NIM/Nama : 19622026/Muhammad Althariq Fairuz
# Tanggal 5-10-2022
# Deskripsi : Mencari faktor prima dari suatu bilangan N dengan N >1

#KAMUS
#N,jmlh = int

#ALGORITMA
faktor = 0
N = int(input('Masukkan nilai N : '))
print ( 'Faktor primanya adalah :',end='')
for i in range (2,N+1):
    if ( N % i == 0):
        jmlh = 0
        for j in range (1,i+1):
            if (i % j == 0) :
                jmlh += 1 
        if jmlh == 2 : #Jika bilangan tersebut habis dibagi 1 dan dirinya sendiri (total hanya 2 pembagian),maka bilangan tersebut prima
            print (i,end='.')













