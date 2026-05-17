def semua_sama(tuple_input):
    return len(set(tuple_input)) <= 1
tA = (90, 90, 90, 90)
tB = (90, 80, 90, 90)
tC = ('a', 'a', 'a')
tD = (1,)
print(semua_sama(tA))
print(semua_sama(tB))
print(semua_sama(tC))
print(semua_sama(tD))