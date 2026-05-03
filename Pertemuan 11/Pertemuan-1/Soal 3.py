>>> import math
>>> saldo_awal = 200000000
>>> saldo_yang_diinginkan = 400000000
>>> bunga_per_tahun = 0.10
>>> tahun = math. log(saldo_yang_diinginkan / saldo_awal) / math.log(1 + bunga_per_tahun)
>>> t_rounded = math.ceil(tahun)
>>> print(f"waktu yang erika butuhkan adalah {t_rounded} tahun")
waktu yang erika butuhkan adalah 8 tahun
>>> 