#Judul program : Menghitung luas segitiga

# KAMUS
# alas = float,berupa input nilai alas segitiga yang diinput oleh user
# tinggi = float,berupa input nilai tinggi yang diinput oleh user
#luas = merupakan hasil kali antara alas dan tinggi lalu dibagi 2

#ALGORITMA
alas = float(input("Masukan nilai alas (dalam m) : ")) #User menginput nilai alas dalam satuan meter
tinggi = float(input("Masukan nilai tinggi segitiga (dalam meter) : ")) #Selanjutnya,user akan menginput nilai tinggi segitiga 
luas = 0.5*alas*tinggi #luas segitiga diperoleh dari hasil kali alas dan tinggi lalu dibagi 2
print ("Luas segitiga (dalam m2) adalah : ",luas,"m2") #output berupa nilai luas segitiga