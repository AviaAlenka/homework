n = int(input("количество строк: "))
m = int(input("количество столбцов: "))
value = int(input("значения: "))
stroki = []
def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.insert(i, [value]*int(m))
    return matrix
matrix = get_matrix(n, m, value)
print(matrix)