def suma_elementos_matriz(m):
    suma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            suma = suma + m[i][j]
    return suma

m = []

m2 = [[1, 2, 3],
      [2, 2, 2],
      [1, 2, 3],
      [1, 2, 3]]

resultado1 = suma_elementos_matriz(m)
print(resultado1)