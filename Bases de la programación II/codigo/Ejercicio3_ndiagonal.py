#Ejercicio 3: n_diagonal

"""
DESCRIPCIÓN DE MI PROCESO DE ABSTRACCIÓN:

Estructura conceptual de la problemática:
1. Identificar la forma de almnacenar en una lista todos los elementos que no pertenezcan a la diagonal
    1.1 toda coordenada en la matriz perteneciente a la diagonal cumple la condición i=j
2. Sumar los elementos diferentes a 0 en esa lista y observar si es mayor al parametro 'n'
3. Entregar True si es menor y False si es mayor a n dicha suma.

Solución conceptual de la problematica:
1. Crear un bucle con otro indexado, para entregar de forma granulada cada elemento de la matriz.
2. generar una dentro del bucle de segundo orden, e integrar en una variable cada elemento que cumpla con dicha condicionalidad
3.contar el número de elementos que integra la lista
4. finalmente se compara la variable con el parametro n
"""
'Solución en codigo:'

def n_diagonal(m,n):
    lista_no_ceros= []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if  i!=j:
                if m[i][j]!=0:
                    lista_no_ceros.append(m[i][j])
    numero_en_lista= len(lista_no_ceros)
    return numero_en_lista<=n

m_diagonal = [[1, 0, 0],
[0, 7, 0],
[0, 0, 3]]
assert(n_diagonal(m_diagonal, 0) == True)
m_no_diagonal = [[1, 0, 2],
[0, 7, 0],
[0, 0, 3]]
assert(n_diagonal(m_no_diagonal, 1) == True)
m_no_diagonal = [[1, 0, 2],
[0, 7, 0],
[0, 3, 3]]
assert(n_diagonal(m_no_diagonal, 2) == True)
m_no_diagonal = [[0, 0, 2],
[0, 7, 0],
[2, 3, 3]]
assert(n_diagonal(m_no_diagonal, 2) == False)

#pruebas borde adicionales:

prueba_de_borde1 = [[1]] 
assert( n_diagonal(prueba_de_borde1, 1) == True)

prueba_de_borde2 = [] 
assert( n_diagonal(prueba_de_borde2, 1) == True)

prueba_de_borde3 = m_diagonal = [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]] 
assert( n_diagonal(prueba_de_borde3, 1) == True)

prueba_de_borde4 = m_diagonal = [[1, -1, 0],
                                [0, 0, 0],
                                [0, 0, 0]] 
assert( n_diagonal(prueba_de_borde4, 1) == True)


prueba_de_borde5 = m_diagonal = [[1, -1, 0],
                                [0, 0, 0],
                                [0, 0, 0]] 
assert( n_diagonal(prueba_de_borde5, -1) == False)
