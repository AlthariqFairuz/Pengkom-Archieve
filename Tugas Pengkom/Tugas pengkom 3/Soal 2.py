#Program : Mnejumlahkan bilang kelipatan lima sampai N kali
#KAMUS
#n,jmlh : int

#Algoritma
jmlh = 0
n = int(input ('Masukkan nilai N/batas akhir kelipatan : '))
for kelipatan5 in range (1,n+1):
    if kelipatan5 % 5 == 0:
        jmlh += kelipatan5
print (f'Jumlah bilangan kelipatan 5 dalam rentang 1 sampai {n} adalah {jmlh} ')
