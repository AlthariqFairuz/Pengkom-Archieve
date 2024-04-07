#Judul Program : Menghitung jarak tempuh

#KAMUS
#Kecepatan = float,berupa input kecepatan (dalam m/s)
#Waktu = float,berupa waktu yang ditempuh selama perjalanan
#Jarak = float,hasil perkalian antara kecepatan dan waktu

#ALGORITMA
kecepatan = float(input("Masukan kecepatan (dalam m/s) : ")) #User menginputkan nilai kecepatan
waktu = float(input("Masukan waktu (dalam sekon) : ")) #Selanjutnya,user akan menginputkan nilai waktu
jarak = kecepatan*waktu #Jarak diperoleh dari hasil kali antara kecepatan dan waktu yang telah diinput user
print ("Maka,jarak tempuhnya adalah : ", jarak,"m") #output berupa hasil jarak dalam meter