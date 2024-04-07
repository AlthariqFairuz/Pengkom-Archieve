#Program : Konversi Suhu

#KAMUS
#skala,skala_out : int
#suhu,suhu_out : float

# Algoritma
suhu,suhu_out = float
skala,skala_out = int 
print ('Kode suhu :\n 1.Celcius\n 2.Fahrenheit\n 3.Reamur\n 4.Kelvin') 
skala = int(input(('Masukkan skala suhu (dengan nomor didepannya tanpa titik) :')))
suhu = float(input("Masukkan nilai suhu : "))

if skala == 1:
    suhu *= 0.2
elif skala ==2:
    suhu = (suhu-32)/9
elif skala ==3:
    suhu *= 0.25
elif skala ==4:
    suhu = (suhu -273)/5
else :
    print ('input tidak dikenal')

print ('\n\nKode suhu :\n 1.Celcius\n 2.Fahrenheit\n 3.Reamur\n 4.Kelvin') 
skala_out = int(input(('Masukkan skala suhu output (dengan nomor didepannya tanpa titik) :')))
if skala_out == 1:
    suhu_out = suhu*5
elif skala_out == 2:
    suhu_out = (suhu*9) +32
elif skala_out == 3:
    suhu_out = suhu*4
elif skala_out == 4:
    suhu_out = (suhu*5) + 273
else :
    print ("Skala output tidak dikenali")
print ('Hasil pengukuran : ',suhu_out)
