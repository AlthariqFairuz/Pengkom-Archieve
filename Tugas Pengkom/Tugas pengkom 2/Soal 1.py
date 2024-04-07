#Program : menghitung kekuatan gempa bumi
#KAMUS :

#SR,Float

#Algoritma :
SR = float(input("Masukan nilai Skala Richter Gempa : "))
if (0 < SR < 2.0):
    print ("Kekuatan gempa : Micro")
if (2.0<= SR < 3.9 ):
    print ("Kekuatan gempa : Minor")
if (3.9 <= SR < 4.9):
    print ("Kekuatan gempa : Light")
if (4.9 <= SR < 5.9):
    print ("Kekuatan gempa : Moderate")
if (5.9 <= SR < 6.9):
    print ("Kekuatan gempa : Strong")
if (6.9 <= SR < 7.9):
    print ("Kekuatan gempa : Major")
if (SR >= 7.9):
    print ("Kekuatan gempa : Great")
if (SR >= 10.0 or SR <= 0.0):
    print ("Input Anda Salah")


