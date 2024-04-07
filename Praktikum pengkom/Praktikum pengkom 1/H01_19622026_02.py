#NIM/Nama : 19622026/Muhammad Althariq Fairuz
#Tanggal : 12 September 2022
#Deskripsi : Pembagian kelas 
NIM = int(input("Masukan 3 digit terakhir NIM Anda :"))

if NIM >=1 and NIM <= 100:
    if NIM % 2 == 0:
        print ("Anda di kelas K2")
    else:
        print ("Anda di kelas K1")

if NIM >=101 and NIM <=200:
    if NIM % 2 == 0:
        print ("Anda di kelas K4")
    else:
        print ("Anda di kelas K3")

if NIM >=201 and NIM <= 300:
    if NIM % 2 == 0:
        print ("Anda di kelas K6")
    else:
        print ("Anda di kelas K5")

if NIM >300:
    if NIM % 2 == 0:
        print ("Anda di kelas K8")
    else:
        print ("Anda di kelas K7")
if NIM <1:
    print ("NIM anda tidak terdaftar")


