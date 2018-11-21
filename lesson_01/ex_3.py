# По введенным пользователем координатам двух точек вывести
# уравнение прямой, проходящей через эти точки.

point1_x = int(input("Введите координату X1"))
point1_y = int(input("Введите координату Y1"))
point2_x = int(input("Введите координату X2"))
point2_y = int(input("Введите координату Y2"))

k = (point1_y - point2_y) * (point1_x - point2_x)
b = point2_y - k * point2_x

print(f"y = {k}x + {b}")
