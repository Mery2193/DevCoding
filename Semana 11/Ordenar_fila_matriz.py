# Función de ordenación Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila_index):
    # Ordenar la fila específica usando Bubble Sort
    bubble_sort(matriz[fila_index])

# Matriz bidimensional de ejemplo (3x3)
matriz = [
    [2, 9, 5],
    [7, 3, 6],
    [1, 4, 8]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Especificar qué fila ordenar (por ejemplo, la segunda fila, índice 1)
fila_a_ordenar = 1

# Ordenar la fila especificada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de ordenar la fila
print("\nMatriz Después de Ordenar la Fila:")
for fila in matriz:
    print(fila)
