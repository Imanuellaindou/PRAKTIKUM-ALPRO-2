def hitung_ips(jumlah_mata_kuliah, nilai_mata_kuliah):
    total_nilai = 0
    total_sks = 0
    for nilai in nilai_mata_kuliah:
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print(f"Nilai '{nilai}' tidak valid. Mengabaikan mata kuliah ini.")
            continue

        total_nilai += bobot * 3
        total_sks += 3

    if total_sks == 0:
        return 0
    ips = total_nilai / total_sks
    return ips

jumlah_mata_kuliah = int(input("Berapa jumlah mata kuliah? "))
nilai_mata_kuliah = []

for i in range(jumlah_mata_kuliah):
    nilai = input(f"Nilai MK {i + 1}: ").upper()
    nilai_mata_kuliah.append(nilai)

ips = hitung_ips(jumlah_mata_kuliah, nilai_mata_kuliah)
print(f"Nilai IPS anda semester ini {ips:.2f}")