#Ejercicio 7: Suma matrices.

def crear_matriz_zeros(n_filas, n_columnas):
    m = list()
    for i in range(n_filas):
        m.append(list())
        for j in range(n_columnas):
            m[i].append([0])
    return m

def suma_matrices(m1, m2):
    if m1 == [] and m2 == []:
        return 'matriz vacia'
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]) :
        n_filas = len(m1)
        n_columnas = len(m1[0])
        m = crear_matriz_zeros(n_filas, n_columnas)
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m[i][j] = m1[i][j] + m2[i][j]
        return m
    if m1 == [] and m2 == []:
        return 'matriz vacia'
    else:
        return 'la estructura de la matriz no cumple las propiedades de la suma'

mat1 = [[2, 0, 0, 0],
[3, 2, 0, 0],
[3, 3, 2, 0],
[3, 3, 3, 2]]
mat2 = [[2, 3, 3, 3],
[0, 2, 3, 3],
[0, 0, 2, 3],
[0, 0, 0, 2]]
resultado = [[4, 3, 3, 3], [3, 4, 3, 3], [3, 3, 4, 3], [3, 3, 3, 4]]
assert(suma_matrices(mat1, mat2) == resultado)

mat1 = [[1]]
mat2 = [[2]]
assert(suma_matrices(mat1, mat2) == [[3]] )

mat1 = []
mat2 = []
assert(suma_matrices(mat1, mat2) == 'matriz vacia')
