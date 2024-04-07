#Porgram : menghitung hari
#KAMUS
#tahun,bulan,bulan_akhir,tanggal,tanggal_akhir,jmlh_hari : int

#Algoritma
tahun = int(input('Masukan tahun : '))
tanggal = int (input('Masukkan tanggal :'))
bulan = int(input('Masukkan bulan (dalam angka) : '))
tanggal_akhir = int (input('Masukkan tanggal akhir :'))
bulan_akhir = int(input('Masukkan bulan akhir (dalam angka) : '))
jmlh_hari = int
if bulan == bulan_akhir and bulan_akhir > 0 and bulan > 0:
    jmlh_hari = tanggal_akhir - tanggal
    print ('\nJumlah hari : ',jmlh_hari)
elif bulan_akhir > bulan and (bulan_akhir > 0 and bulan > 0) :
    if bulan in range (1,8,2) or bulan_akhir in range (8,13,2) :
        jmlh_hari = (31-tanggal) + tanggal_akhir
    elif bulan in range (4,7,2) or bulan_akhir in range (9,12,2):
        jmlh_hari = (30-tanggal) + tanggal_akhir
    elif bulan == 2:
        if (tahun % 4 ==0 and tahun % 100 != 0) or tahun % 400 ==0 :
            jmlh_hari = (29-tanggal)+ tanggal_akhir
        else :
            jmlh_hari = (28-tanggal) + tanggal_akhir
    else :
        print ('Input anda salah')
for h in range ((bulan + 1),(bulan_akhir)):
    if h in range (1,8,2) or h in range (8,13,2):
        jmlh_hari += 31
    elif h in range (4,7,2) or h in range (9,12,2):
        jmlh_hari += 30
    elif h == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 ==0:
            jmlh_hari += 29
        else :
            jmlh_hari += 28 

if jmlh_hari < 0 :
    print ('Inputan anda salah')
else:
    print ('\nJumlah hari :',jmlh_hari)