# Codingan 1
jumlah_hari_bulan_di_tahun_2020 = [31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if 1 <= bulan <= 12:
        print (f"Jumlah hari: (jumlah_hari_bulan_di_tahun_2020[bulan]")
    else:
        print("Bulan tidak valid")
except:
    print("Masukkan bulan harus berbentuk angka")

# Codingan 2
jumlah_hari_bulan_di_tahun_2020 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if 1 <= bulan <= 12:
        print(f"Jumlah hari: {jumlah_hari_bulan_di_tahun_2020[bulan-1]}")
    else:
        print("Bulan tidak valid")
except:
    print("Masukkan bulan harus berbentuk angka")
    