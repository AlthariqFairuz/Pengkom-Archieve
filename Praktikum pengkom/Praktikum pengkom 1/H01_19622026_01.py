#NIM/Nama : 19622026/Muhammad Althariq Fairuz
#Tanggal : 12 September 2022
#Deskripsi : Mencari keuntungan barang terbesar

a_dasar = int(input("Masukan harga dasar barang A: ")) # Input harga dasar barang A 
a_jual = int(input("Masukan harga jual barang A: ")) # Input harga jual barang A 
b_dasar = int(input("Masukan harga dasar barang B: ")) # Input harga dasar barang B 
b_jual = int(input("Masukan harga jual barang B: ")) # Input harga jual barang B 
c_dasar = int(input("Masukan harga dasar barang C: ")) # Input harga dasar barang C 
c_jual =  int(input("Masukan harga jual barang C: ")) # Input harga jual barang C 
untung_a = a_jual - a_dasar
untung_b = b_jual - b_dasar
untung_c = c_jual - c_dasar

if untung_a > untung_b : #jika barang A untungnya paling tinggi
    if untung_a > untung_c :
        print ("Barang yang harus ditawarkan adalah barang A")

if untung_b > untung_a : #jika barang B untugnnya paling tinggi
    if untung_b > untung_c :
        print ("Barang yang harus ditawarkan adalah barang B")

if untung_c > untung_a : #jika barang C untungnya paling tinggi
    if untung_c > untung_b :
        print ("Barang yang harus ditawarkan adalah barang C")

if untung_a == untung_b == untung_c : #jika keuntungan barang sama
    print ("Keuntungan masing masing barang sama")

if untung_a<0 or untung_b<0 or untung_c<0: 
    if untung_a == untung_b :
        print ("Untung A sama dengan B")

    if untung_a == untung_c :
        print ("Untung A sama dengan C")

    if untung_c == untung_b :
        print ("Harga B sama dengan C")
