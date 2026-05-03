gaji_per_jam = float(input("Masukkan gaji per jam yang diinginkan: "))
jam_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))
total_jam = jam_per_minggu * 5
pendapatan_kotor = gaji_per_jam * total_jam

pajak = 0.14 * pendapatan_kotor
pendapatan_bersih = pendapatan_kotor - pajak

biaya_pakaian_aksesoris = 0.10 * pendapatan_bersih 
biaya_alat_tulis = 0.01 * pendapatan_bersih

sisa_uang = pendapatan_bersih - biaya_pakaian_aksesoris - biaya_alat_tulis

total_sedekah = 0.25 * sisa_uang
anak_yatim = 0.30 * total_sedekah
kaum_dhuafa = 0.70 * total_sedekah

print("\nRincian Pendapatan Budi:")
print(f"1. Pendapatan sebelum pajak: Rp {pendapatan_kotor:.2f}")
print(f"2. Pendapatan setelah pajak: Rp {pendapatan_bersih:.2f}")
print(f"3. Uang untuk membeli pakaian & aksesoris: Rp {biaya_pakaian_aksesoris:.2f}")
print(f"4. Uang untuk membeli alat tulis: Rp {biaya_alat_tulis:.2f}")
print(f"5. Total sedekah: Rp {total_sedekah:.2f}")
print(f"6. Sedekah untuk anak yatim: Rp {anak_yatim:.2f}")
print(f"7. Sedekah untuk kaum dhuafa: Rp {kaum_dhuafa:.2f}")