import string
def menerima_file(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            isi_file = file.read()
            return isi_file
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return None
def menampilkan_kata_unik(teks):
    translator = str.maketrans('', '', string.punctuation)
    teks_bersih = teks.translate(translator)
    kata_kata = teks_bersih.split()
    kata_unik = set(kata_kata)
    return kata_unik
if __name__ == "__main__":
    nama_file = input("Masukkan nama file: ")
    isi_file = menerima_file(nama_file)
    if isi_file is not None:
        kata_unik = menampilkan_kata_unik(isi_file)
        print("Kata-kata unik dalam file:")
        for kata in kata_unik:
            print(kata)