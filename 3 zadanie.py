#1: Считать три числа и вывести их сумму.

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
#2: Считать длины двух катетов и вывести площадь треугольника.

a = int(input())
b = int(input())
print(0.5 * a * b)
#3: Определить время по прошедшим минутам.

n = int(input())
hours = (n // 60) % 24
minutes = n % 60
print(hours, minutes)
#4: Расчет длины шнурка. Переведем в функцию.

def calculate_lace_length(a, b, l, N):
    import math
    # Расстояние по горизонтали между дырочками в одном ряду
    horizontal_distance = b * (N - 1)
    # Расстояние по вертикали между рядами
    vertical_distance = a
    # Общая длина шнурка
    length = 0
    for i in range(N):
        # Расстояние между дырочками в двух рядах
        horizontal_offset = i * b
        # Расстояние по гипотенузе между дырочками
        segment_length = math.sqrt(horizontal_offset**2 + vertical_distance**2)
        length += 2 * segment_length  # так как шнур проходит туда и обратно
    # Добавляем свободные концы
    total_length = length + 2 * l
    return total_length
#5: Наименьшее из трех чисел.

def min_of_three(a, b, c):
    print(min(a, b, c))
#6: Проверка цвета клеток шахматной доски.

def same_color(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print("Да")
    else:
        print("Нет")
#7: Проверка високосного года.

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Да")
    else:
        print("Нет")
#8: Количество совпадающих чисел.

def count_matches(a, b, c):
    if a == b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)
#9: Можно ли отломить часть шоколадки.

def can_break(n, m, k):
    if (k % n == 0 and k // n <= m) or (k % m == 0 and k // m <= n):
        print("Да")
    else:
        print("Нет")