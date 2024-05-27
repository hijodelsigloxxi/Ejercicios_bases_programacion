#Ejercicio 2: Suma elementos de una matriz

def suma_elementos_matriz(m):
    suma = 0
    for i in range(len(m)):
        if len(m[i]) == len(m[0]):
            for j in range(len(m[0])):
                suma = suma + m[i][j]
        elif len(m[i]) != len(m[0]):
            for j in range(len(m[i])):
                suma = suma + m[i][j]
    return suma

m = [[1, 2, 3],
     [2, 2, 2],
     [1, 2, 3]]

m2 = [[1, 2, 3],
      [2, 2, 2],
      [1, 2, 3],
      [1, 2, 3]]
m3 = [[1, 2, 3],
      [2, 2, 2],
      [1, 2, 3],
      [1, 2, 3, 2]]
m4 = []

assert(suma_elementos_matriz(m) == 18)
assert(suma_elementos_matriz(m2) == 24)
assert(suma_elementos_matriz(m3) == 26)
assert(suma_elementos_matriz(m4) == 0)