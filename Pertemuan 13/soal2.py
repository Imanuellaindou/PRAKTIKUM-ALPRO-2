data_diri = (
    'Imanuella Indou',
    '71241110',
    'Manokwari, Papua Barat'
)
nama, nim, alamat = data_diri
print(f"Data          : {data_diri}")
print(f"NIM           : {nim}")
print(f"NAMA          : {nama}")
print(f"ALAMAT        : {alamat}")
nim_tuple = tuple(nim)
print(f"NIM Tuple     : {nim_tuple}")
nama_depan = nama.split()[0].lower()
nama_depan_tuple = tuple(nama_depan)
print(f"Nama Depan    : {nama_depan_tuple}")
nama_terbalik = tuple(nama.split()[::-1])
print(f"Nama Terbalik : {nama_terbalik}")