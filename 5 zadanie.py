#1. Все квадраты натуральных чисел, не превосходящие N
N = int(input("Введите N (≥2): "))
i = 1
while i * i <= N:
    print(i * i)
    i += 1
#2. Наименьший натуральный делитель числа N, отличный от 1
N = int(input("Введите число (≥2): "))

for i in range(2, N + 1):
    if N % i == 0:
        print(i)
        break
#3. Наибольшая степень двойки, не превосходящая N, без функции возведения в степень
N = int(input("Введите N: "))
power = 0
value = 1

while value * 2 <= N:
    value *= 2
    power += 1

print(power, value)
#4. Номер дня, когда пробег спортсмена станет не меньше y
x = float(input("Введите начальный пробег x: "))
y = float(input("Введите целевой пробег y: "))

day = 1
distance = x

while distance < y:
    distance *= 1.1
    day += 1

print(day)
#5. Количество чисел в последовательности (без завершающего 0)
count = 0

while True:
    num = int(input())
    if num == 0:
        break
    count += 1

print(count)
#6. Среднее значение элементов последовательности, завершающейся 0
total = 0
count = 0

while True:
    num = int(input())
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    print(total / count)
else:
    print(0)  # или сообщение о пустой последовательности
#8. Сколько элементов больше предыдущего
prev = int(input())
count = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num > prev:
        count += 1
    prev = num

print(count)
#8 Наибольшее количество подряд идущих равных элементов
prev = int(input())
max_len = 1
curr_len = 1

while True:
    num = int(input())
    if num == 0:
        break
    if num == prev:
        curr_len += 1
    else:
        curr_len = 1
    if curr_len > max_len:
        max_len = curr_len
    prev = num

print(max_len)
