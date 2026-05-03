angka1 = int(input("Masukkan angka pertama:"))
angka2 = int(input("Masukkan angka kedua:"))
angka3 = int(input("Masukkan angka ketiga:"))

if angka1 < angka2 and angka1 < angka3:
    print("Terkecil: ", angka1)
if angka2 < angka1 and angka2 < angka3:
    print("Terkecil: ", angka2)
if angka3 < angka1 and angka3 < angka2:
    print("Terkecil: ", angka3)
