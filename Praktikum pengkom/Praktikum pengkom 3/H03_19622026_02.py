# NIM/ Nama : 19622026/Muhammad Althariq Fairuz
# Tanggal : 20 oktober 2022
# Deskripsi : Menentukan lampu mana yang hidup dan mati berdasarkan input

# KAMUS :
# total,nekantombol : int
# lampu : array of int

#ALGORITMA
total = int(input("Masukkan banyak lampu: "))
nekantombol = int(input("Masukkan jumlah berapa kali anda nekan tombol : "))

lampu = [0 for i in range(total)]

for i in range(nekantombol):
    tombol = int(input(f"Masukkan tombol yang ditekan ke-{i+1} : ")) #masukkan tombol nomor berapa yang ditekan
    if tombol == 1:
        for j in range(tombol+1): #pake +1 biar nyampe ke lampu selanjutnya
            if lampu[j] == 0: #jika sama sama mati
                lampu[j] = 1
            else:
                lampu[j] = 0 #jika lamupu kedua hidup
    elif tombol == len(lampu): #jika tombol terakhir ditekan
        for j in range(tombol-2,tombol):#kita ambil lampu kedua terakhir dan terakhir untuk di swap
            if lampu[j] == 0:
                lampu[j] = 1
            else:
                lampu[j] = 0
    else: 
        for j in range(tombol-2,tombol+1): 
            #misalkan yang ditekan tombol ketiga dari empat tombol,maka tombol ketiga itu index terakhir dari array lampu,
            #dan tombol 3 yang kita inginkan itu berada pada index ke-2 di array,jadinya kita harus kurangin 2 nilai tombolnya,dan maxnya di tombol yang kita tekan (yang bertukar lampu index 1,2,dan 3 dari total 4 lampu)
            if lampu[j] == 0:
                lampu[j] = 1
            else:
                lampu[j] = 0
print(f"Keadaan akhir rangkaian lampu adalah {lampu} ")