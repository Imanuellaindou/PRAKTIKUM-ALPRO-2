# Codingan 1
suhu = int(input("Silahkan masukkan suhu anda: "))
try:
    if suhu > 38:
        print("Tubuh anda mengalami demam")
    elif suhu > 37.5:
        print("Tubuh anda tidak mengalami demam")
except:
    print("Suhu harus berbentuk angka")
    
# Codingan 2
bilangan = int(input("Silahkan masukkan suatu bilangan: "))
try:
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except:
    print("Masukkan suatu bilangan berbentuk angka")

# Codingan 3
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua "))
c = int(input("Masukkan bilangan ketiga: "))
try:
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except:
    print("Masukkan bilangan terbesar harus berbentuk angka")
    
    