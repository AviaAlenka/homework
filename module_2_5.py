n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))
value = int(input("значения: "))
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.insert(i, [value]*int(m))
    return matrix
matrix = get_matrix(n, m, value)
print("Получим матрицу", str(n) + "х" + str(m) + ":")
print(matrix)