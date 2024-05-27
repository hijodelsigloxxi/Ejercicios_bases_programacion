#Ejercicio 6 : matriz transpuesta

def es_transpuesta(m1,m2):
    diagonal_matriz1 = []
    diagonal_matriz2 = []
    inferior1_diagonal = []
    inferior2_diagonal = []
    superior1_diagonal = []
    superior2_diagonal = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if i == j:
                diagonal_matriz1.append(m1[i][j])
                diagonal_matriz2.append(m2[j][i])
            elif i > j:
                inferior1_diagonal.append(m1[i][j])
                superior2_diagonal.append(m2[j][i])
            elif i < j:
                superior1_diagonal.append(m1[i][j])
                inferior2_diagonal.append(m2[j][i])
    if inferior1_diagonal == superior2_diagonal and  inferior2_diagonal == superior1_diagonal and diagonal_matriz1 == diagonal_matriz2 :
        return True
    else:
        return False

mat1 = [[2, 0, 0, 0],
[3, 2, 0, 0],
[3, 3, 2, 0],
[3, 3, 3, 2]]
mat2 = [[2, 3, 3, 3],
[0, 2, 3, 3],
[0, 0, 2, 3],
[0, 0, 0, 2]]
mat3 = [[1, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]]
mat4 = [[0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1]]
assert(es_transpuesta(mat1, mat2))
assert(not es_transpuesta(mat3, mat4))

print(es_transpuesta(mat1, mat2))

