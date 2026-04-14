def analisis_teks(kalimat):
    kalimat_lower = kalimat.lower()
    total_vokal = 0
    for huruf in 'aiueo':
        total_vokal += kalimat_lower.count(huruf)
    kata_list = kalimat.split()
    jumlah_kata = len(kata_list)
    kata_terbalik = ' '.join(reversed(kata_list))
    kata_kapital = kalimat.title()

    print(f"Kalimat asli  : {kalimat}")
    print(f"Jumlah vokal  : {total_vokal}")
    print(f"Jumlah kata   : {jumlah_kata}")
    print(f"Urutan terbalik: {kata_terbalik}")
    print(f"Huruf kapital : {kata_kapital}")
kalimat_input = input("Masukkan kalimat: ")
analisis_teks(kalimat_input)
