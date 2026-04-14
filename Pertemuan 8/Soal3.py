import re
def ekstrak_informasi(teks):
    pola_email = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    daftar_email = re.findall(pola_email, teks)
    pola_telp = r'08\d{2}[\-\s]?\d{4}[\-\s]?\d{4}'
    daftar_telp = re.findall(pola_telp, teks)
    pola_url = r'https?://[\w./\-?=&%#]+'
    daftar_url = re.findall(pola_url, teks)
    print("=== Hasil Ekstraksi ===")
    print(f"Email ditemukan   : {len(daftar_email)} buah")
    for e in daftar_email:
        print(f"  - {e}")
    print(f"\nTelepon ditemukan : {len(daftar_telp)} buah")
    for t in daftar_telp:
        print(f"  - {t}")
    print(f"\nURL ditemukan     : {len(daftar_url)} buah")
    for u in daftar_url:
        print(f"  - {u}")

teks_contoh = """
Hubungi kami di info@ukdw.ac.id atau admin@example.com
Telp: 0812-3456-7890 atau 0821 9876 5432
Website: https://www.ukdw.ac.id dan http://example.com/halaman
Email kedua: support@test.org
"""
ekstrak_informasi(teks_contoh)


