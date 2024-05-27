#ejercicio 8: sumar bordes

def suma_bordes(m):
    suma = 0
    if len(m)>=1 and isinstance(m[0],list):
        for i in range(len(m)):
            if i == 0:
                for j in range(len(m[0])):
                    suma = suma + m[i][j]
            elif i != 0 and i != len(m)-1:
                for j in range(len(m[0])):
                    if j == 0 or j == len(m[0]) - 1:
                        suma = suma + m[i][j]
            elif i == len(m) - 1:
                for j in range(len(m[0])):
                    suma = suma + m[i][j]
            else:
                return ' no se corresponde a las propiedades necesarias'
    else:
        return 'no es una matriz'
    return suma
mat1 = [[2, 0, 8, 0],
        [3, 2, 0, 6],
        [3, 3, 2, 0],
        [3, 3, 3, 2]]
assert (suma_bordes(mat1) == 33)
mat2 = [[1, 2, 3, 4],
[3, 2, 0, 6],
[3, 3, 2, 0],
[3, 3, 3, 2],
[3, 3, 3, 2]]
assert (suma_bordes(mat2) == 38)

mat2=[[1,4,5]]           
suma_bordes(mat2)

mat2=[3 , 4]           
suma_bordes(mat2)