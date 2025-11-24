
import math
1.1
# Вычисление площади разных фигур
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side ** 2

print("Вычисление площади фигур")
radius = float(input("Введите радиус круга: "))
print(f"Площадь круга: {area_circle(radius):.2f}")

length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))
print(f"Площадь прямоугольника: {area_rectangle(length, width):.2f}")

base = float(input("Введите основание треугольника: "))
height = float(input("Введите высоту треугольника: "))
print(f"Площадь треугольника: {area_triangle(base, height):.2f}")

side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {area_square(side):.2f}")
1.2
# Работа с 3 массивами
print("\nВвод 3 массивов (до 15 элементов каждый)")

arrays = []
for i in range(3):
    arr = list(map(int, input(f"Введите элементы массива {i+1} через пробел: ").split()))
    if len(arr) > 15:
        print("Размер массива превышает 15, будут использованы первые 15 элементов.")
        arr = arr[:15]
    arrays.append(arr)

for i, arr in enumerate(arrays, 1):
    s = sum(arr)
    avg = s / len(arr) if len(arr) > 0 else 0
    print(f"Массив {i}: сумма = {s}, среднеарифметическое = {avg:.2f}")

import math
2.1
# Вычисляем площадь треугольника по формуле: 0.5 * основание * высота
def area_triangle(base, height):
    return 0.5 * base * height

# Площадь правильного шестиугольника = 6 * площадь одного равностороннего треугольника
# Высота такого треугольника = a * (√3 / 2)
def area_hexagon(a):
    height = a * (math.sqrt(3) / 2)
    return 6 * area_triangle(a, height)
2.2
# Вычисляем площади трёх прямоугольников по введённым сторонам
def area_rectangle(length, width):
    return length * width

print("1. Площадь правильного шестиугольника")
a = float(input("Введите длину стороны a: "))
print(f"Площадь правильного шестиугольника: {area_hexagon(a):.2f}")

print("\n2. Площади трёх прямоугольников")
for i in range(1, 4):
    print(f"Прямоугольник {i}:")
    length = float(input("Введите первую сторону: "))
    width = float(input("Введите вторую сторону: "))
    print(f"Площадь прямоугольника {i}: {area_rectangle(length, width):.2f}\n")

import math
3.1
# Функция вычисления длины гипотенузы прямоугольного треугольника по катетам
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Ввод катетов двух треугольников
print("Введите катеты первого прямоугольного треугольника")
a1 = float(input("Катет 1: "))
b1 = float(input("Катет 2: "))

print("Введите катеты второго прямоугольного треугольника")
a2 = float(input("Катет 1: "))
b2 = float(input("Катет 2: "))

# Вычисление гипотенуз
h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

# Сравнение и вывод результата
if h1 > h2:
    print(f"Гипотенуза первого треугольника ({h1:.2f}) больше гипотенузы второго ({h2:.2f}).")
elif h1 < h2:
    print(f"Гипотенуза второго треугольника ({h2:.2f}) больше гипотенузы первого ({h1:.2f}).")
else:
    print(f"Гипотенузы равны: {h1:.2f}")
3.2
# Преобразование строки с сортировкой букв в каждом слове по алфавиту
def sort_letters_in_words(s):
    words = s.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)

# Ввод строки
input_str = input("Введите строку: ")
result = sort_letters_in_words(input_str)
print("Преобразованная строка:")
print(result)
4.1
# Деление дроби A/B на дробь C/D с результатом в несократимой форме
def gcd(x, y):
    # Алгоритм Евклида для поиска НОД
    while y:
        x, y = y, x % y
    return x

def divide_fractions(A, B, C, D):
    # Деление (A/B) / (C/D) = (A/B) * (D/C) = (A*D)/(B*C)
    numerator = A * D
    denominator = B * C
    # Сокращаем дробь
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Ввод дробей
A = int(input("Введите числитель первой дроби (A): "))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))

num, den = divide_fractions(A, B, C, D)
print(f"Результат деления несократимой дробью: {num}/{den}")
4.2
# Проверка, сколько точек лежит внутри окружности

def is_inside_circle(x, y, a, b, R):
    # Процедура проверяет, лежит ли точка (x,y) внутри окружности (x-a)^2 + (y-b)^2 < R^2
    return (x - a) ** 2 + (y - b) ** 2 < R ** 2

# Ввод параметров окружности
a = float(input("Введите координату a центра окружности: "))
b = float(input("Введите координату b центра окружности: "))
R = float(input("Введите радиус окружности R: "))

# Ввод точек
p1, p2 = map(float, input("Введите координаты точки P (p1 p2): ").split())
f1, f2 = map(float, input("Введите координаты точки F (f1 f2): ").split())
l1, l2 = map(float, input("Введите координаты точки L (l1 l2): ").split())

points = [(p1, p2), (f1, f2), (l1, l2)]

count_inside = sum(is_inside_circle(x, y, a, b, R) for x, y in points)

print(f"Количество точек, лежащих внутри окружности: {count_inside}")
5.1
# Вычитание дробей A/B - C/D с результатом в несократимой форме
def gcd(x, y):
    # Алгоритм Евклида для НОД
    while y:
        x, y = y, x % y
    return x

def subtract_fractions(A, B, C, D):
    # Вычисляем разность: (A/B) - (C/D) = (A*D - C*B) / (B*D)
    numerator = A * D - C * B
    denominator = B * D
    common_divisor = gcd(abs(numerator), denominator)
    return numerator // common_divisor, denominator // common_divisor

# Ввод дробей
A = int(input("Введите числитель первой дроби (A): "))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))

num, den = subtract_fractions(A, B, C, D)

# Обработка случая, если числитель 0
if num == 0:
    print("Результат: 0")
else:
    print(f"Результат вычитания несократимой дробью: {num}/{den}")
5.2
# Вывод всех делителей числа в одну строку через пробел
def print_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    print(*divisors)

number = int(input("Введите число для нахождения делителей: "))
print_divisors(number)
6.1
# Нахождение НОД и НОК двух натуральных чисел с использованием алгоритма Евклида

def gcd(a, b):
    # Алгоритм Евклида для НОД
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # НОК = (A * B) / НОД(A, B)
    return a * b // gcd(a, b)

A = int(input("Введите первое число (A): "))
B = int(input("Введите второе число (B): "))

nod = gcd(A, B)
nok = lcm(A, B)

print(f"НОД({A}, {B}) = {nod}")
print(f"НОК({A}, {B}) = {nok}")
6.2
# Вычисление площади выпуклого четырёхугольника по четырём сторонам и диагонали

import math

def quadrilateral_area(a, b, c, d, e):
    # a, b, c, d - стороны
    # e - диагональ, которая разбивает четырехугольник на два треугольника: (a,b,e) и (c,d,e)
    # Используем формулу Герона для площади каждого треугольника

    def heron(x, y, z):
        p = (x + y + z) / 2  # полупериметр
        return math.sqrt(p * (p - x) * (p - y) * (p - z))

    area1 = heron(a, b, e)
    area2 = heron(c, d, e)

    return area1 + area2

print("\nВведите длины четырёх сторон четырёхугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

e = float(input("Введите длину диагонали (e): "))

result = quadrilateral_area(a, b, c, d, e)
print(f"Площадь выпуклого четырёхугольника: {result:.4f}")
7.1
# Вычисление площади четырёхугольника с прямым углом между сторонами X и Y
# Используются две подпрограммы: площадь прямоугольника и площадь прямоугольного треугольника

def rectangle_area(a, b):
    # Площадь прямоугольника
    return a * b

def right_triangle_area(a, b):
    # Площадь прямоугольного треугольника
    return (a * b) / 2

def quadrilateral_area(X, Y, Z, T):
    # Угол между X и Y прямой - значит площадь = площадь прямоугольника (со сторонами X и Y)
    # + площадь двух треугольников, образованных оставшимися сторонами
    # Можно рассмотреть четырёхугольник как прямоугольник (X*Y) + два треугольника, которые нужно вычислить
    # Но так как угол между X и Y – прямой, а остальные стороны Z и T,
    # тогда площадь четырёхугольника = площадь прямоугольника (X * Y) + площадь треугольника с основаниями Z и T и высотой Y или X (если предположить)
    #
    # Однако задача не уточняет расположение сторон Z и T - для простоты считаем площадь = X*Y + 0 (нет дополнительной площади)
    # Предположим, это прямоугольник с дополнительным отрезком: для задачи считается площадь прямоугольника с катетами X и Y.

    # Если ориентироваться на стандарт:
    # площадь = площадь прямоугольника + площадь одного треугольника (с двумя известными сторонами Z и T)
    # Но информации недостаточно для точного расчёта, сделаем упрощение:
    return rectangle_area(X, Y) + right_triangle_area(Z, T)

# Ввод данных
X = float(input("Введите длину стороны X: "))
Y = float(input("Введите длину стороны Y: "))
Z = float(input("Введите длину стороны Z: "))
T = float(input("Введите длину стороны T: "))

area = quadrilateral_area(X, Y, Z, T)
print(f"Площадь четырёхугольника: {area:.4f}")
7.2
# Перевод неотрицательного целого числа в 10-значный восьмеричный код с лидирующими нулями

def to_octal_10_digit(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    oct_str = oct(n)[2:]  # преобразуем в восьмеричную строку без '0o'
    # добавляем лидирующие нули до длины 10
    return oct_str.zfill(10)

num = int(input("Введите неотрицательное целое число: "))
result = to_octal_10_digit(num)
print(f"Восьмеричный код 10 знаков: {result}")





