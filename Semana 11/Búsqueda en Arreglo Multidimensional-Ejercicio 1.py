def buscar_valor(matriz, valor):
    """Busca un valor en la matriz y devuelve su posición (fila, columna)"""
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna  # Retorna la posición si se encuentra
    return None  # Retorna None si no se encuentra el valor

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [5, 12, 8],
    [21, 3, 7],
    [14, 18, 9]
]

# Mostrar la matriz en pantalla
print("📌 Matriz:")
for fila in matriz:
    print(fila)

# Solicitar al usuario un valor a buscar
valor_a_buscar = int(input("\nIngrese el valor a buscar en la matriz: "))

# Realizar la búsqueda en la matriz
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"\n✅ El valor {valor_a_buscar} se encontró en la posición (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"\n❌ El valor {valor_a_buscar} no se encuentra en la matriz.")
