#NIM/Nama : 19622026/Muhammad Althariq Fairuz
#Tanggal : 12 September 2022
#Deskripsi : Berapa lama waktu berlari

print ("Masukkan waktu mulai!\n")

jam = int(input("Masukan jam mulai :"))
menit = int(input("Masukan menit mulai :"))
detik = int(input("Masukan detik mulai :\n"))

print ("Masukan waktu selesai!\n")

jam_S = int(input("Masukan jam selesai :"))
menit_S = int(input("Masukan menit selesai :"))
detik_S = int(input("Masukan detik selesai :\n"))

#konversi ke detik
waktu_mulai = jam*3600 + menit*60 + detik
waktu_selesai = jam_S*3600 + menit_S*60 + detik_S
total_lari = waktu_selesai - waktu_mulai #baik waktu mulai maupun waktu selesai dikonversikan ke detik,total_lari hasilnya berupa detik

#durasi
durasi_jam = total_lari//3600 #total detik dibagi 3600 utk dikonversi ke jam dan digenapin pakai //
durasi_menit = (total_lari%3600)//60 #sisa dari pembagian jam tadi dikonversikan ke menit dan dibulatkan dengan //60
durasi_detik = total_lari%60 #sisa detik yang tersisa setelah dikonversikan ke menit akan dimodulo dengan 60 (modulo = sisa pembagian)

if durasi_jam<0 or durasi_menit<0 or durasi_detik<0:
    print ("Data yang anda masukan salah")
else :
    print ("Total waktu lari adalah : ",durasi_jam,"jam",durasi_menit,"menit",durasi_detik,"detik")








