"""Importamos la libreria random"""

import random

"""Esta funcion sirve para generar la matriz """

def generar_matriz(N):
    matriz = []
    for _ in range(N):
        fila = [random.randint(0, 9) for _ in range(N)]
        matriz.append(fila)
    return matriz


"""La funcion para imprimir una matriz en la consola """
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

"""Funcion suma las filas y las columnas de la matriz"""

def sumar_filas_columnas(matriz):
    N = len(matriz)
    sumas_filas = []
    sumas_columnas = []
    for i in range(N):
        suma_fila = sum(matriz[i])
        suma_columna = sum(matriz[j][i] for j in range(N))
        sumas_filas.append(suma_fila)
        sumas_columnas.append(suma_columna)
    return sumas_filas, sumas_columnas


"""Esta funcion imprime las sumas de filas y columnas"""


def imprimir_sumas(sumas_filas, sumas_columnas):
    print("Suma de cada fila:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i + 1}: {suma}")
    print("Suma de cada columna:")
    for i, suma in enumerate(sumas_columnas):
        print(f"Columna {i + 1}: {suma}")


"""Solicitar al usuario el tamaño de la matriz"""


while True:
    try:
        N = int(input("Ingrese el tamaño de la matriz cuadrada: "))
        break
    except ValueError:
        print("Error: Ingrese un numero entero por favor.")

"""Genera la matriz y la mostramos"""


matriz = generar_matriz(N)
print("matriz generada:")
imprimir_matriz(matriz)

"""Calcula la suma de filas y columnas"""

sumas_filas, sumas_columnas = sumar_filas_columnas(matriz)

"""Imprimime la suma de filas y columnas"""

imprimir_sumas(sumas_filas, sumas_columnas)
