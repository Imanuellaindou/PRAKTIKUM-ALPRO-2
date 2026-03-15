def ganjil(batasBawah, batasAtas):
    deret = []
    if batasBawah < batasAtas:
        for i in range(batasBawah, batasAtas + 1):
            if i % 2 != 0:
                deret.append(i)
    else:
        for i in range(batasBawah, batasAtas - 1, -1):
            if i % 2 != 0:
                deret.append(i)

    return deret

batasBawah = int(input("Masukkan batas bawah: "))
batasAtas = int(input("Masukkan batas atas: "))

hasil_ganjil = ganjil(batasBawah, batasAtas)
print("Deret bilangan ganjil:", ", ".join(map(str, hasil_ganjil)))
