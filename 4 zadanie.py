# 1. Вывести все числа от A до B (A ≤ B)
A, B = map(int, input().split())
for num in range(A, B + 1):
    print(num, end=' ')
print()

# 2. Вывести все числа от A до B в порядке возрастания или убывания
A, B = map(int, input().split())
if A < B:
    for num in range(A, B + 1):
        print(num, end=' ')
else:
    for num in range(A, B - 1, -1):
        print(num, end=' ')
print()

# 3. Вывести все нечётные числа от A до B (A > B), в порядке убывания
A, B = map(int, input().split())
for num in range(A, B - 1, -1):
    if num % 2 != 0:
        print(num, end=' ')
print()

# 4. Сумма N чисел, вводимых пользователем
N = int(input())
total = 0
for _ in range(N):
    total += int(input())
print(total)

# 5. Сумма кубов чисел от 1 до n
n = int(input())
sum_cubes = 0
for i in range(1, n + 1):
    sum_cubes += i ** 3
print(sum_cubes)

# 6. Вычисление n! без math
n = int(input())
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)

# 7. Сумма факториалов от 1! до n! без math, один цикл
n = int(input())
sum_factorials = 0
current_factorial = 1
for i in range(1, n + 1):
    current_factorial *= i
    sum_factorials += current_factorial
print(sum_factorials)

# 8. Лесенка из n ступенек
n = int(input())
for i in range(1, n + 1):
    print(''.join(str(j) for j in range(1, i + 1)))
#9 Количество чисел из ряда
n = int(input())
a, b = 0, 1
sum_fibonacci = a
for _ in range(n - 1):
    sum_fibonacci += b
    a, b = b, a + b

print( sum_fibonacci)
#10 Сумма чисел
N = int(input())
K = int(input())
a, b = 0, 1
for _ in range(K - 1):
    a, b = b, a + b

sum_fibonacci = 0
for _ in range(N):
    sum_fibonacci += a
    a, b = b, a + b

print(sum_fibonacci)