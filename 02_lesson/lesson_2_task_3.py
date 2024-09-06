import math

def square(side):
    return math.ceil(side * side)


side = float(input('Введите значение стороны квадрата :'))
if (side < 0):
    print('Размерность стороны не может быть отрицательной')
else:
    print(f'Площадь квадрата - {square(side)}')
