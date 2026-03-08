def cek_angka(a, b, c):
    if a == b or a == c or b == c:
        return False
    elif a + b == c or a + c == b or b + c == a:
        return True
    else:
        return False
print(cek_angka(2, 3, 1))
print(cek_angka(4, 5, 3))
print(cek_angka(5, 3, 2))
print(cek_angka(1, 4, 2))