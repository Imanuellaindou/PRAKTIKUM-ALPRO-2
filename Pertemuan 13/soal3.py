filename = input("Enter a file name: ")
hitung_jam = {}
try:
    with open(filename) as file:
        for baris_email in file:
            if baris_email.startswith("From "):
                komponen_waktu = baris_email.split()[5]
                jam = komponen_waktu.split(":")[0]
                hitung_jam[jam] = hitung_jam.get(jam, 0) + 1
    for jam in sorted(hitung_jam, key=int):
        print(jam, hitung_jam[jam])

except FileNotFoundError:
    print("File tidak ditemukan!")