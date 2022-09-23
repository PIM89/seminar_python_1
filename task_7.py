# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or z) == (not x and not y and not z):
                f = True
            else:
                f = False
            print(x, y, z, f)