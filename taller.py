# Crea una matriz llena de 0s del tamaño de 2 matrices que entran como parametro. Array[n:n] of int
def zero_matrix(a: list, b: list) -> list:
    result_matrix = []
    for i in range(len(a)):
        result_matrix.append([])
        for j in range(len(b)):
            result_matrix[i].append(0)

    return result_matrix


# Multiplica 2 matrices cuadradas
def matrix_multiply(a: list, b: list) -> list:
    result_matrix = zero_matrix(a, b)
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(a)):
                # Se usa k para acceder a la posicion en la fila o columna
                result_matrix[i][j] += a[i][k] * b[k][j]

    return result_matrix


# Espacio para probar la correctitud del algoritmo
print(matrix_multiply([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
