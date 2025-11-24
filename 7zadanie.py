1.1
# Ввод количества элементов
N = int(input("Введите количество элементов массива: "))

# Ввод массива
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

# Проверка, что количество введённых элементов совпадает с N
if len(arr) != N:
    print("Ошибка: количество введённых элементов не совпадает с N.")
else:
    # Нахождение максимального элемента
    max_element = max(arr)
    print("Максимальный элемент:", max_element)

    # Вывод массива в обратном порядке
    print("Массив в обратном порядке:", arr[::-1])
1.2

# Ввод количества элементов
N = int(input("Введите количество элементов массива: "))

# Ввод массива действительных чисел
arr = list(map(float, input("Введите элементы массива через пробел: ").split()))

if len(arr) != N:
    print("Ошибка: количество введённых элементов не совпадает с N.")
else:
    # Вычисляем среднее арифметическое всех элементов
    average = sum(arr) / N

    # Заменяем нули на среднее арифметическое
    arr = [average if x == 0 else x for x in arr]

    print("Массив после замены нулей на среднее арифметическое:")
    print(arr)
2.1
# Нахождение минимального элемента и его индекса

N = int(input("Введите количество элементов массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

if len(arr) != N:
    print("Ошибка: количество введённых элементов не совпадает с N.")
else:
    min_element = min(arr)
    min_index = arr.index(min_element)
    print(f"Минимальный элемент: {min_element}")
    print(f"Индекс минимального элемента: {min_index}")
2.2
# Разделение массива на два: положительные и остальные

arr2 = []
arr3 = []

for x in arr:
    if x > 0:
        arr2.append(x)
    else:
        arr3.append(x)

print("Массив с положительными элементами:", arr2)
print("Массив с остальными элементами:", arr3)
3.1
# Сумма элементов с нечётными индексами

D = list(map(int, input("Введите элементы массива D через пробел: ").split()))
n = len(D)

sum_odd_indices = 0
for i in range(1, n, 2):  # перебор индексов 1, 3, 5, ...
    sum_odd_indices += D[i]

print("Массив D:", D)
print("Сумма элементов с нечётными индексами:", sum_odd_indices)
3.2
# Замена элементов массива длиной 8

arr = list(map(int, input("Введите 8 элементов массива через пробел: ").split()))

if len(arr) != 8:
    print("Ошибка: нужно ввести ровно 8 элементов.")
else:
    for i in range(8):
        if arr[i] < 15:
            arr[i] = arr[i] * 2
    print("Преобразованный массив:", arr)
4.1
# Нахождение максимального элемента массива и его порядкового номера

arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

max_element = arr[0]
max_index = 0  # нумерация с 0, если нужна с 1 — добавить +1 при выводе

for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
        max_index = i

print(f"Максимальный элемент: {max_element}")
print(f"Порядковый номер максимального элемента: {max_index + 1}")
4.2
# Массив из нечётных чисел исходного массива, вывод в порядке убывания

odd_numbers = [x for x in arr if x % 2 != 0]

if len(odd_numbers) == 0:
    print("Нечётных чисел в массиве нет.")
else:
    odd_numbers.sort(reverse=True)
    print("Массив нечётных чисел в порядке убывания:")
    print(odd_numbers)
5.1
# Ввод массива из 10 целых чисел
arr = list(map(int, input("Введите 10 целых чисел через пробел: ").split()))

# Вывод пар отрицательных чисел, стоящих рядом
print("Пары соседних отрицательных чисел:")
found_pairs = False
for i in range(len(arr) - 1):
    if arr[i] < 0 and arr[i+1] < 0:
        print(f"({arr[i]}, {arr[i+1]}) на позициях {i+1} и {i+2}")
        found_pairs = True
if not found_pairs:
    print("Таких пар нет.")
5.2
# Создание нового массива с уникальными элементами
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)
6.1
print("Массив без повторяющихся элементов:")
print(unique_arr)

# Ввод массива из 10 целых чисел
arr = list(map(int, input("Введите 10 целых чисел через пробел: ").split()))

# Найти среднеарефметическое
average = sum(arr) / len(arr)
print(f"Среднеарефметическое: {average}")

# Максимум массива
max_element = max(arr)

# Подсчёт элементов
count_less_than_max = sum(1 for x in arr if x < max_element)
count_greater_than_avg = sum(1 for x in arr if x > average)

print(f"Количество элементов меньше максимального ({max_element}): {count_less_than_max}")
print(f"Количество элементов больше среднеарефметического: {count_greater_than_avg}")
6.2
# 2. Определить сумму чисел, которые > 5
sum_greater_5 = sum(x for x in arr if x > 5)
print(f"Сумма чисел, больших 5: {sum_greater_5}")
7.1
# Ввод массива целых чисел
arr = list(map(int, input("Введите целые числа через пробел: ").split()))

# Сумма элементов с четными номерами (индексами) и произведение элементов с нечетными номерами
# Индексация с 0, значит, "четные номера" - элементы с индексами 0, 2, 4 ...
sum_even_index = sum(arr[i] for i in range(0, len(arr), 2))
prod_odd_index = 1
for i in range(1, len(arr), 2):
    prod_odd_index *= arr[i]

print(f"Сумма элементов с четными номерами: {sum_even_index}")
print(f"Произведение элементов с нечетными номерами: {prod_odd_index}")
7.2
# Перестановка минимального и максимального элементов
min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

# Меняем местами
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(f"Массив после перестановки мин и макс элементов: {arr}")



