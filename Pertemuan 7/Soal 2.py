def bilangan_prima(n):
    if n <= 2:
        return 2
    for i in range(n - 1, 1, -1):
        prima = True
        for j in range(2, i):
            prima = False
            break
        if prima:
            return i
n = int(input("Masukkan bilangan bulat: "))
print(f"input n=(n), maka prima terdekta < {n} adalah {bilangan_prima(n)}")