#Ejercicio 9: solo 1:

''' Mi objetivo es descifrar la forma en la que puedo descomponer la matriz en diferentes variables, una por cada fila
y otra por cada columna, cada una de estas variables debe sumar los elementos que contiene, si cada una de estas variables
nos da como resultado un 1, eso quiere decir que la matriz cumple las propiedades del ejercicio y nos da verdadera, sino
no las cumple y nos da falsa.'''

def solo_1(m):
    variables_filas = {}
    variables_columnas = {}
    for i in range(len(m)):
        nombre_variable = f'variable_fila {i}'
        variables_filas[nombre_variable] = 0
    for i in range(len(m[0])):
        nombre_variable = f'variable_columna {i}'
        variables_columnas[nombre_variable] = 0
    num = -1
    for i in variables_filas:
        num = num + 1
        for j in range(len(m[0])):
            variables_filas[i] = variables_filas[i] + m[num][j]
    num = -1
    for i in variables_columnas:
        num = num + 1
        for j in range(len(m)):
            variables_columnas[i] = variables_columnas[i] + m[j][num]
    for i in  variables_filas.values():
        if i != 1:
            return False
    for i in  variables_columnas.values():
        if i != 1:
            return False
    return True

m1 = [[0, 0, 1],
[1, 0, 0],
[0, 1, 0]]
assert(solo_1(m1))

m2 = ([[0, 0, 1],
[1, 0, 0],
[0, 0, 1]])
assert(not solo_1(m2))

m3 = ([[0, 1],
[1, 0]])
assert(solo_1(m3))
m4 = ([[0, 0],
[1, 0]])
assert(not solo_1(m4))
m5 = ([[1, 1, 0],
[0, 0, 0],
[0, 0, 1]])
assert(not solo_1(m5))
    
    
    
