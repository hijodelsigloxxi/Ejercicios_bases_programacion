#Ejercicio 2: Suma elementos de una matriz

def suma_elementos_matriz(m):
    suma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            suma = suma + m[i][j]
    return suma

m = [[1, 2, 3],
     [2, 2, 2],
     [1, 2, 3]]

m2 = [[1, 2, 3],
      [2, 2, 2],
      [1, 2, 3],
      [1, 2, 3]]

assert(suma_elementos_matriz(m) == 18)
assert(suma_elementos_matriz(m2) == 24)


