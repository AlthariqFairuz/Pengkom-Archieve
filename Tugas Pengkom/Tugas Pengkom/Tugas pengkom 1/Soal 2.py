#Judul program : Mencari keliling lingkaran

#KAMUS
#phi = ketetapan dalam lingkaran (3.14 atau 22/7)
#jari-jari = float,berupa input jari-jari lingkaran dalam meter
#Keliling = merupakan hasil kali dari dua kali jari-jari dengan phi

#ALGORITMA
phi = 3.14 #phi merupakan ketetapan 
jarijari = float(input("Masukan nilai jari-jari lingkaran (dalam meter): ")) #User menginput nilai jari-jari
keliling = 2*jarijari*phi #keliling diperoleh dari 2 kali jari jari dikalikan dengan phi
print ("Keliling lingkaran (dalam meter) adalah : ",keliling,"m") #output berupa keliling lingkaran