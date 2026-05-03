import re
def konversi_tanggal(tanggal_str):
    pola = r'^(\d{2})-(\d{2})-(\d{4})$'
    cocok = re.match(pola, tanggal_str)
    if not cocok:
        print("Format tanggal tidak valid!")
        print("Gunakan format: DD-MM-YYYY (contoh: 14-04-2026)")
        return None
    hari  = cocok.group(1)
    bulan = cocok.group(2)
    tahun = cocok.group(3)
    if int(hari) < 1 or int(hari) > 31:
        print("Hari tidak valid (harus 01-31)")
        return None
    if int(bulan) < 1 or int(bulan) > 12:
        print("Bulan tidak valid (harus 01-12)")
        return None
    tanggal_baru = f"{tahun}/{bulan}/{hari}"
    print(f"Format asli  : {tanggal_str}")
    print(f"Format baru  : {tanggal_baru}")
    return tanggal_baru
tanggal_input = input("Masukkan tanggal (DD-MM-YYYY): ")
konversi_tanggal(tanggal_input)


