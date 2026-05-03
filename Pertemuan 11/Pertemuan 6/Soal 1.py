def perkalian(x, y):
    if x == 0 or y == 0:
        return 0 
    else:
        persamaan = f"{x} x {y} = "
        total = 0
        for i in range(x):
            total += y
            persamaan += f"{y}"
            if i < x - 1:
                persamaan += " + "
    persamaan += f" = {total}"
    return persamaan 
    
print(perkalian(6, 5))
print(perkalian(7, 10))