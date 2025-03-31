# --- Escritura de Archivo de Texto ---

# Abrimos (o creamos) el archivo en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales únicas de Samanta Rios
archivo.write("Hoy sentí que conecté con el código de una forma diferente, más intuitiva.\n")
archivo.write("Me emociona pensar que algún día podré automatizar tareas de mi vida diaria.\n")
archivo.write("Este pequeño avance me recuerda que cada paso suma, aunque sea corto.\n")

# Cerramos el archivo después de escribir
archivo.close()


# --- Lectura del Archivo de Texto ---

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos línea por línea usando un bucle
print("Contenido del archivo:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() elimina saltos de línea adicionales al imprimir
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
