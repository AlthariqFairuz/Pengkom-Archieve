#Judul program : Rata rata dari 5 data

# KAMUS
# data1 = float,berupa nilai data yang merupakan inputan dari user  
# data2 = float,berupa nilai data yang merupakan inputan dari user  
# data3 = float,berupa nilai data yang merupakan inputan dari user  
# data4 = float,berupa nilai data yang merupakan inputan dari user  
# data5 = float,berupa nilai data yang merupakan inputan dari user  
#average = float,rata rata dari semua data

#ALGORITMA
data1 = float(input("Masukan nilai data 1 : ")) #User memasukan data 1 sampai data 5 berurutan
data2 = float(input("Masukan nilai data 2 : "))
data3 = float(input("Masukan nilai data 3 : "))
data4 = float(input("Masukan nilai data 4 : "))
data5 = float(input("Masukan nilai data 5 : "))
average = (data1+data2+data3+data4+data5)/5 #rata rata diperoleh dari jumlah keseluruahan data lalu dibagi 5
print ("Rata-rata data adalah : ",average) #output berupa hasil rata rata data