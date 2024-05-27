#ejercicio 1: imprimir matriz

def imprimir_matriz(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j])

m = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
 
imprimir_matriz(m)