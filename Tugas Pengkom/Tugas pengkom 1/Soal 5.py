#Judul program : Perhitungan harga kelereng

#KAMUS : 
#kelereng 1 = int, merupakan inputan jumlah kelereng merah yang ingin dibeli user 
#kelereng 2 = int, merupakan inputan jumlah kelereng hijau yang ingin dibeli user 
#kelereng 3 = int, merupakan inputan jumlah kelereng hitam yang ingin dibeli user 

#ALGORITMA
print ("="*3,"TOKO KELERENG","="*3)
Merah = 10 
Hijau = 15 
Hitam = 20 

kelereng1 = int(input("Masukan jumlah kelereng merah :"))   
kelereng2 = int(input("Masukan jumlah kelereng hijau :"))
kelereng3 = int(input("Masukan jumlah kelereng hitam :"))
total = (Merah*kelereng1)+(Hijau*kelereng2)+(Hitam*kelereng3) 
print ("Total pembelian : ",total, "sen")