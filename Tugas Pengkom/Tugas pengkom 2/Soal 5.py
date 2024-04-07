#Program : Billangan pallindrom
#KAMUS 
#ALGORITMA
var = 0 
angka = input('Masukkan bilangan bulat : ')
if len(angka) % 2 == 0:
    for a in range (0,int(len(angka)/2)) :
        if angka [a] == angka [int(-(a+1))]:
            var += 1
else :
    for a in range (0,int((len(angka)-1)/2)):
        if angka [a] == angka [int(-(a+1))]:
            var += 1

if var == (len(angka) // 2):
    print ('Angka input termasuk palindrom')
else : 
    print ('Angka input bukan palindrom')
    