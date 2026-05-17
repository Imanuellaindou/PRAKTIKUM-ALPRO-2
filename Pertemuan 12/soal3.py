filename = input("Masukkan nama file: ")
email_counts = {}
try:
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1:
                    email = words[1]
                    email_counts[email] = email_counts.get(email, 0) + 1
    print("\nJumlah Email Tiap Pengirim:")
    for email, jumlah in email_counts.items():
        print(email, ":", jumlah)
except FileNotFoundError:
    print("File tidak ditemukan!")