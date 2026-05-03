tinggi_badan = float(input("Masukkan tinggi badan anda (dalam meter): "))
berat_badan = float(input("Masukkan berat badan anda (kg): "))
hitung_bmi = berat_badan / (tinggi_badan ** 2)
print(f"BMI Anda adalah: {hitung_bmi:.2f}")