def tiga_bilangan_terbaik(list_bilangan):
    list_berurut = sorted(list_bilangan, reverse=True)
    bilangan_tertinggi = list_berurut[:3]
    return bilangan_tertinggi

bilangan = [7, 14, 23, 28, 90]
hasil = tiga_bilangan_terbaik(bilangan)
print(hasil)