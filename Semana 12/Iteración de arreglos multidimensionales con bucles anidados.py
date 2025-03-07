# Crear una matriz 3D para almacenar las temperaturas
# La estructura es: [ciudad][día de la semana][semana]
temperaturas = [
    [  # Ciudad: Loja
        [22, 23, 24],  # Semana 1: Lunes, Martes, Miércoles
        [21, 22, 23],  # Semana 2: Lunes, Martes, Miércoles
        [20, 21, 22]   # Semana 3: Lunes, Martes, Miércoles
    ],
    [  # Ciudad: Ambato
        [18, 19, 20],  # Semana 1: Lunes, Martes, Miércoles
        [17, 18, 19],  # Semana 2: Lunes, Martes, Miércoles
        [21, 22, 23]   # Semana 3: Lunes, Martes, Miércoles
    ],
    [  # Ciudad: Manta
        [28, 29, 30],  # Semana 1: Lunes, Martes, Miércoles
        [27, 28, 29],  # Semana 2: Lunes, Martes, Miércoles
        [30, 31, 32]   # Semana 3: Lunes, Martes, Miércoles
    ]
]

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(matriz, ciudades):
    for ciudad in range(len(matriz)):  # Iterar sobre las ciudades
        print(f"Promedios para la ciudad de {ciudades[ciudad]}:")
        for semana in range(len(matriz[ciudad])):  # Iterar sobre las semanas
            suma_temperaturas = sum(matriz[ciudad][semana])  # Sumar las temperaturas de los 3 días
            promedio = suma_temperaturas / len(matriz[ciudad][semana])  # Calcular el promedio
            print(f"  Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")
        print("")  # Línea en blanco para separar las ciudades

# Nombres de las ciudades
ciudades = ["Loja", "Ambato", "Manta"]

# Llamar a la función para calcular y mostrar los promedios
calcular_promedio_temperaturas(temperaturas, ciudades)

