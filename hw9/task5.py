def quadratic_equation(a, b, c):
    x1 = x2 = None

    def calc_result(a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root, root
        else:
            return None, None

    x1, x2 = calc_result(a, b, c)
    return x1, x2

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

roots = quadratic_equation(a, b, c)
if roots[0] is not None and roots[1] is not None:
    print(f"Корені рівняння: x1 = {roots[0]}, x2 = {roots[1]}")
else:
    print("Рівняння не має дійсних коренів.")
