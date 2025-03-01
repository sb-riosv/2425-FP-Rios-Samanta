def quicksort(fila):
    """Ordena una lista (fila de la matriz) usando el algoritmo QuickSort"""
    if len(fila) <= 1:
        return fila  # Si la fila tiene 1 o 0 elementos, ya está ordenada
    else:
        pivote = fila[len(fila) // 2]  # Elegimos el pivote como el elemento del medio
        izquierda = [x for x in fila if x < pivote]  # Elementos menores que el pivote
        centro = [x for x in fila if x == pivote]  # Elementos iguales al pivote
        derecha = [x for x in fila if x > pivote]  # Elementos mayores que el pivote
        return quicksort(izquierda) + centro + quicksort(derecha)

# Definir una matriz 3x3 con valores numéricos desordenados
matriz = [
    [15, 3, 9],
    [88, 42, 17],
    [31, 26, 50]
]

# Mostrar la matriz original
print("📌 Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (por ejemplo, la segunda fila - índice 1)
fila_a_ordenar = 1

# Ordenar la fila usando QuickSort
matriz[fila_a_ordenar] = quicksort(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila
print("\n✅ Matriz después de ordenar la fila seleccionada:")
for fila in matriz:
    print(fila)
