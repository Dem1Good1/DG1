1.1
# Вычислить сумму и число положительных элементов матрицы A[N,N],
# находящихся над главной диагональю (i < j)

def sum_and_count_positive_above_diag(A):
    n = len(A)
    total_sum = 0
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] > 0:
                total_sum += A[i][j]
                count += 1
    return total_sum, count
1.2
# 2. В каждой строке матрицы B[N,M] найти максимальный и минимальный элементы
# и поменять их с первым и последним элементами строки соответственно

def swap_min_max_in_rows(B):
    n = len(B)
    m = len(B[0]) if n > 0 else 0
    for i in range(n):
        row = B[i]
        # Найдем индексы мин и макс элементов
        min_index = row.index(min(row))
        max_index = row.index(max(row))

        # Поменять max с первым элементом
        row[0], row[max_index] = row[max_index], row[0]

        # Если минимальный элемент был в позиции 0 (которая теперь занята max),
        # обновим min_index, чтобы корректно заменить последний элемент
        if min_index == 0:
            min_index = max_index

        # Поменять min с последним элементом
        row[-1], row[min_index] = row[min_index], row[-1]

    return B
2.1
# Проверка, является ли квадратная матрица магическим квадратом
def is_magic_square(matrix):
    n = len(matrix)
    if n == 0:
        return False

    # Вычисляем сумму первой строки как эталон
    target_sum = sum(matrix[0])

    # Проверяем суммы всех строк
    for i in range(1, n):
        if sum(matrix[i]) != target_sum:
            return False

    # Проверяем суммы всех столбцов
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False

    return True
2.2
# Перестановка первого и последнего столбцов прямоугольной матрицы A[N, M]
def swap_first_last_columns(A):
    n = len(A)
    if n == 0:
        return A
    m = len(A[0])
    if m < 2:
        # Если столбцов меньше 2, перестановка невозможна
        return A

    for i in range(n):
        A[i][0], A[i][m-1] = A[i][m-1], A[i][0]

    return A
3.1
# Проверка, является ли квадратная матрица симметричной относительно главной диагонали
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):  # проверяем только сверху или снизу от диагонали,
                                 # так как симметрия — a[i][j] == a[j][i]
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
3.2
# Перестановка строк и столбцов вещественной матрицы n x m,
# чтобы один из наибольших элементов оказался в верхнем левом углу
def move_max_to_top_left(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0

    # Ищем координаты максимального элемента (одного из них)
    max_val = matrix[0][0]
    max_pos = (0, 0)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)

    max_i, max_j = max_pos

    # Меняем местами строки: ставим строку с max элементом на первую позицию
    matrix[0], matrix[max_i] = matrix[max_i], matrix[0]

    # Теперь меняем местами столбцы, чтобы max элемент оказался в [0][0]
    for i in range(n):
        matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]

    return matrix
4.1
# Поиск строки с наибольшей и с наименьшей суммой элементов в прямоугольной матрице
def find_min_max_sum_rows(matrix):
    min_sum = float('inf')
    max_sum = float('-inf')
    min_row = None
    max_row = None

    for row in matrix:
        s = sum(row)
        if s > max_sum:
            max_sum = s
            max_row = row
        if s < min_sum:
            min_sum = s
            min_row = row

    return (min_row, min_sum), (max_row, max_sum)
4.2
# Замена отрицательных элементов на 0, положительных на 1 в квадратной матрице,
# вывод нижней треугольной матрицы (включая главную диагональ)
def modify_and_print_lower_triangle(matrix):
    n = len(matrix)

    # Модифицируем матрицу
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 0:
                matrix[i][j] = 1
            else:
                # Если элемент равен 0, оставим его как есть
                pass

    # Вывод нижней треугольной матрицы
    for i in range(n):
        row_str = ""
        for j in range(n):
            if j <= i:
                row_str += f"{matrix[i][j]} "
            else:
                row_str += "  "  # пустые места в верхней треугольнике
        print(row_str.rstrip())
5.1
# Упорядочить по возрастанию элементы каждой строки матрицы n x m
def sort_rows(matrix):
    return [sorted(row) for row in matrix]
5.2
# Заменить в каждой строке минимальный элемент
# на 0 если он чётный, или на 1 если нечётный (все элементы различны)
def replace_min_elements(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0

    # Создаем копию матрицы, чтобы не менять исходную
    new_matrix = [row[:] for row in matrix]

    for i in range(n):
        row = new_matrix[i]
        min_val = min(row)
        min_index = row.index(min_val)

        # Проверяем чётность минимального элемента и заменяем
        if int(min_val) % 2 == 0:
            new_matrix[i][min_index] = 0
        else:
            new_matrix[i][min_index] = 1

    return new_matrix
6.1
# Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент и в каждом столбце наименьший.

def find_max_in_rows_and_min_in_columns(matrix):
    n = len(matrix)
    max_in_rows = [max(row) for row in matrix]

    min_in_columns = []
    for j in range(n):
        col = [matrix[i][j] for i in range(n)]
        min_in_columns.append(min(col))

    return max_in_rows, min_in_columns
6.2
# Дана действительная квадратная матрица порядка N (N — нечетное).
# Все элементы различны.
# Найти наибольший элемент среди элементов главной и побочной диагоналей
# и поменять его местами с элементом на пересечении диагоналей.

def swap_max_on_diagonals(matrix):
    n = len(matrix)
    center = n // 2  # индекс пересечения главной и побочной диагоналей

    # На главной диагонали: элементы matrix[i][i]
    # На побочной диагонали: matrix[i][n - 1 - i]
    diag_elements = []

    for i in range(n):
        diag_elements.append((matrix[i][i], i, i))                 # главная диагональ
        if i != center:  # избегаем добавлять центр второй раз
            diag_elements.append((matrix[i][n - 1 - i], i, n -1 - i))

    # Наибольший элемент среди диагоналей
    max_val, max_i, max_j = max(diag_elements, key=lambda x: x[0])

    # Позиция пересечения диагоналей
    ci, cj = center, center

    # Меняем элементы местами
    matrix[max_i][max_j], matrix[ci][cj] = matrix[ci][cj], matrix[max_i][max_j]

    return matrix
7.1
# Восстановление симметричной квадратной матрицы по верхнему треугольнику

def restore_symmetric_matrix(arr, n):
    """
    arr - одномерный массив элементов верхнего треугольника (включая главную диагональ)
    n - порядок матрицы
    """
    matrix = [[0]*n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = arr[index]
            matrix[j][i] = arr[index]  # симметрично относительно главной диагонали
            index += 1
    return matrix
7.2
# Формирование массива диагональных элементов, вычисление следа и преобразование матрицы

def diag_array_and_transform(matrix):
    n = len(matrix)
    diag = [matrix[i][i] for i in range(n)]
    trace = sum(diag)

    for i in range(n):
        # Четные строки (индексация с 0, значит строки с i%2==0)
        if i % 2 == 0:
            # Делим элементы строки на след
            matrix[i] = [x / trace for x in matrix[i]]
    return diag, trace, matrix






