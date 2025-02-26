# Función para realizar la búsqueda en la matriz
def buscar_en_matriz(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna  # Retorna la posición (fila, columna)
    return None  # Retorna None si el valor no fue encontrado

# Matriz bidimensional de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que queremos buscar en la matriz
valor_a_buscar = 5

# Llamada a la función de búsqueda
resultado = buscar_en_matriz(matriz, valor_a_buscar)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
