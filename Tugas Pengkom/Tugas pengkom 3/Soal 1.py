#Program :  Membuat deret geometri berdasarkan input a,r,n dan menentukan apakah deret tersebut
#           konvergen atau divergen

#KAMUS
# a,r,n : int 

#ALGORITMA 
G = 0
a = float(input( "Masukkan nilai a :"))
r = float(input( "Masukkan nilai r :"))
n = int(input( "Masukkan nilai n :"))

for x in range (n):
    G += a * (r**x)
if abs (r) < 1: #abs = absolut/mutlak
    E = (a/(1-r))-G
    print ( f"Deret geometri konvergen dengan nilai G : {G}  dan E : {E}")
else :
    print (f'Deret divergen dengan nilai G : {G}')
    