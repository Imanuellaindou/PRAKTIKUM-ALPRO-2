data = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60
}
print("Key\tValue\tItem")
for key, value in data.items():
    print(f"{key}\t{value}\t({key}, {value})")