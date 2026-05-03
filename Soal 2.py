bilangan_list = []

while True:
    try:
        user_input = input("Masukkan bilangan (atau 'done' untuk selesai): ")
        if user_input.lower() == 'done':
            break
        number = float(user_input)
        bilangan_list.append(number)
    except ValueError:
        print("Input tidak valid. Silakan masukkan bilangan atau 'done' .")
        
if bilangan_list:
    rata_rata = sum(bilangan_list) / len(bilangan_list)
    print(f"Rata-rata bilangan: {rata_rata:.2f}")
else:
    print("Tidak ada bilangan yang dimasukkan.")