# NIM/Nama : 19622026/Muhammad Althariq Fairuz
# Tanggal 5-10-2022
# Deskripsi : Mencari jumlah setiap bilangan yang lebih besar dari bilangan tepat sebelumnya
# Program akan berhenti bila mendapat input angka tidak lebih besaer selama 3x berturut turut

#Kamus : 
# jmlh_membesar,jmlh_tdk_membesar,n = int
jmlh_membesar = 0    
jmlh_tdk_membesar = 0
n = 1

#ALGORITMA
while (jmlh_tdk_membesar < 3):
    if ( n % 2 == 1):
        angka_ganjil = int(input(f'Angka ke-{n} : '))
        if n > 1 and angka_ganjil > angka_genap : 
            jmlh_membesar += angka_ganjil
            jmlh_tdk_membesar = 0
        else :
            jmlh_tdk_membesar += 1
    else :
        angka_genap = int(input(f'Angka ke -{n} : '))
        if angka_genap > angka_ganjil :
            jmlh_membesar += angka_genap
            jmlh_tdk_membesar = 0
        else :
            jmlh_tdk_membesar += 1
    n += 1
print (f'Jumlah nilai yang membesar adalah {jmlh_membesar}')






