"""
Nombre: Carlos Stiven Ruiz Rojas
Codigo: 2259629
Descripcion: proyecto ADA I, Asigancion de villa

"""
import numpy as np

def grafo_villas(matrix):
    n = len(matrix)
    resultado = [-1] * n  # El -1 indica que no tiene villa asignada
    resultado[0] = 0  # Aqui asigna la primera villa al primer nodo

    Villas_disponibles = [False] * n  # Este arreglo permite llevar el registro de las villas disponibles


    # Se valida cada fila de la matriz para asignar villas
    for u in range(1, n):
        # Se proceso cada vertice adyacente y se marca que no tiene villa asignada
        for i in range(n):
            if matrix[u][i] == 1 and resultado[i] != -1:
                Villas_disponibles[resultado[i]] = True

        # Se busca la primera villa disponible
        villa = 0
        while villa < n:
            if not Villas_disponibles[villa]:
                break
            villa += 1

        resultado[u] = villa  # Se asigna la primera villa que sea verdadera, es decir que su vertice adyacente tiene una diferente

        # Resetea las villas disponibles para la proxima iteracion
        for i in range(n):
            if matrix[u][i] == 1 and resultado[i] != -1:
                Villas_disponibles[resultado[i]] = False

    return resultado


# A partir de las villas asignadas creamos la matriz de salida de tamaño  N x M
def Crear_matriz_salida(villas):
    num_villas = max(villas) + 1 # Esto toma la cantidad de villas retornadas y le suma uno debido a que inicia desde cero el arreglo
    num_selecciones = len(villas) # Es la cantidad de seleccions 
    S = np.zeros((num_villas, num_selecciones), dtype=int) # Creamos una matriz de ceros de tamaño numero de villas x numero de selecciones que sea de tipo entero

    for seleccion, villa in enumerate(villas): 
        S[villa][seleccion] = 1

    return S

def leer_matrices(file_path):
    matrices = []
    matriz_actual = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Si la línea no está vacía
                fila = list(map(int, line.strip().split()))  # Convertir la línea en una lista de enteros
                matriz_actual.append(fila)
            else:
                if matriz_actual:
                    matrices.append(matriz_actual)
                    matriz_actual = []

    # Asegurarse de agregar la última matriz si hay alguna
    if matriz_actual:
        matrices.append(matriz_actual)

    return matrices

matrices = leer_matrices('matrices.txt')
for matriz in matrices:
    print("\n")
    print(Crear_matriz_salida(grafo_villas(matriz)))
    