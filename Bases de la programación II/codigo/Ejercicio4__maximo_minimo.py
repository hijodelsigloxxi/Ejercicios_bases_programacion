#Ejercicio 4: Máximo y mímnimo de una matriz



'''def max_min(m):
    if m==[]:
        return 'matriz vacía'
    else:
        numero_maximo = m[0][0]
        numero_minimo = m[0][0]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] > numero_maximo:
                    numero_maximo= m[i][j]
                if m[i][j]< numero_minimo:
                    numero_minimo = m[i][j]
    return numero_maximo, numero_minimo'''

def max_min(m):
    if m==[]:
        return 'matriz vacía'
    else:
        numero_maximo = m[0][0]
        numero_minimo = m[0][0]
        for i in range(len(m)):
            if len(m[0]) == len(m[i]):
                for j in range(len(m[0])):
                    if m[i][j] > numero_maximo:
                        numero_maximo= m[i][j]
                    if m[i][j]< numero_minimo:
                        numero_minimo = m[i][j]
            elif len(m[0]) != len(m[i]):
                for j in range(len(m[i])):
                    if m[i][j] > numero_maximo:
                        numero_maximo= m[i][j]
                    if m[i][j]< numero_minimo:
                        numero_minimo = m[i][j]
        return numero_maximo, numero_minimo


m = [[1, 0, 2],
    [0, 7, 0],
    [0, 0, 3]]

m_1_elemento = [[10]]

assert(max_min(m) == (7, 0))
assert(max_min(m_1_elemento) == (10, 10))

#pruebas borde adicionales:

prueba_de_borde1 = [[1]] 
assert( max_min(prueba_de_borde1) == (1,1))

prueba_de_borde2 = [] 
assert( max_min(prueba_de_borde2) == 'matriz vacía')

prueba_de_borde3 = m_diagonal = [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]] 
assert( max_min(prueba_de_borde3) == (0,0))

prueba_de_borde4 = m_diagonal = [[1, -1, 0],
                                [0, 0, 0],
                                [0, 0, 0]] 
assert( max_min(prueba_de_borde4) == (1,-1))

prueba_de_borde4 = m_diagonal = [[-1, -1, -6],
                                [-7, -3, -5],
                                [-6, -9, -4]] 

assert( max_min(prueba_de_borde4) == (-1,-9))

m = [[1, 0, 2],
    [0, 7, 0, 5],
    [0, 0, 3, 6, 2]]
assert(max_min(m) == (7, 0))