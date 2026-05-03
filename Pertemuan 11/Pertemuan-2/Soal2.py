def hitung_f(x):
    return 2 * (x ** 3) + 2 * x * 15 / x

x = int(input("Masukkan nilai x (bilangan bulat): "))
hasil = hitung_f(x)
print(f"Hasil dari f({x}) = {hasil:.2f}")