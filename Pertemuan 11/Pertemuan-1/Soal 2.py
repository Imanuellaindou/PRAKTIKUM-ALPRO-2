SOAL NOMOR 2 

>>> hargaBeliEmas = 650000
>>> beratEmasAwal = 25
>>> hargaBeliTotal = hargaBeliEmas * beratEmasAwal
>>> print(f"Biaya harga beli emas (Rp0: {hargaBeliTotal}")
Biaya harga beli emas (Rp0: 16250000
>>> hargaJualEmas = 685000
>>> hargaJualTotal = hargaJualEmas * beratEmasAwal
>>> print(f"Biaya harga jual emas (Rp): {hargaJualTotal}")
Biaya harga jual emas (Rp): 17125000
>>> KeuntunganRupiah = hargaJualTotal - hargaBeliTotal
>>> print(f"KeuntunganTotal Gerard (Rp): {KeuntunganRupiah}")
KeuntunganTotal Gerard (Rp): 875000
>>> KeuntunganPersen = (KeuntunganRupiah / hargaBeliTotal)*100
>>> print(f"Keuntungan Total Gerard (%): {KeuntunganPersen:.2f}")
Keuntungan Total Gerard (%): 5.38
>>> beratEmasTambahan = 15
>>> hargaBeliEmasTambahan = 685000 * beratEmasTambahan
>>> print(f"Biaya harga beli emas tambahan (Rp): {hargaBeliEmasTambahan}")
Biaya harga beli emas tambahan (Rp): 10275000
>>> totalEmasSekarang = beratEmasAwal + beratEmasTambahan
>>> print(f"Total berat emas sekarang (gr): {totalEmasSekarang}")
Total berat emas sekarang (gr): 40
>>> hargaJualEmasBaru = 715000
>>> hargaJualTotalBaru = hargaJualEmasBaru * totalEmasSekarang
>>> print(f"Biaya harga jual emas baru (Rp): {hargaJualTotalBaru}")
Biaya harga jual emas baru (Rp): 28600000
>>> totalModal = hargaBeliTotal + hargaBeliEmasTambahan
>>> print(f"Total modal beli emas (Rp): {totalModal}")
Total modal beli emas (Rp): 26525000
>>> KeuntunganRupiah = hargaJualTotalBaru - totalModal
>>> print(f"Keuntungan Total Gerard (Rp): {KeuntunganRupiah}")
Keuntungan Total Gerard (Rp): 2075000
>>> KeuntunganPersen = (KeuntunganRupiah / totalModal)*100
>>> print(f"Keuntungan Total Gerard (Rp): {KeuntunganPersen:.2f}%")
Keuntungan Total Gerard (Rp): 7.82%
>>> 

