#Program : Lokasi kuadran
#KAMUS
#X,Y : Float
#ALGORITMA
x = float(input('Masukkan nilai X :' ))
y = float(input('Masukkan nilai Y :'))

if x == 0 and y == 0:
    print (' Titk berada di titik asal')
elif x ==0 and y != 0:
    print ('Titik di sumbu Y')
elif x!=0 and y == 0:
    print ('Titik di sumbu X')
else :
    if x>0 and y > 0:
        print ('Titik di kuadran 1')
    elif x<0 and y > 0:
        print ('Titik di kuadran 2')
    elif x<0 and y < 0:
        print ('Titik di kuadran 3')
    else :
        print ('Titik di kuadran 4')
    