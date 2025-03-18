# Definir la función para calcular el descuento
def calcular_descuento(monto_total, descuento=25):
    """
    Calcula el monto del descuento basado en el monto total de la compra y el porcentaje de descuento.

    :param monto_total: Total de la compra (float o int)
    :param descuento: Porcentaje de descuento (por defecto 25%)
    :return: Monto del descuento
    """
    descuento_monto = monto_total * (descuento / 100)  # Cálculo del descuento
    return descuento_monto


# Programa principal

# Monto de compra para ambas pruebas
monto = 100  # Puedes cambiar este valor

# Primera llamada: descuento predeterminado del 25%
descuento1 = calcular_descuento(monto)
print(f"Monto total: ${monto:.2f}")
print(f"Descuento aplicado (25%): ${descuento1:.2f}")
print(f"Total a pagar: ${monto - descuento1:.2f}\n")

# Segunda llamada: mismo monto pero con un porcentaje de descuento personalizado
descuento_personalizado = 15  # Cambia el porcentaje si deseas probar otro
descuento2 = calcular_descuento(monto, descuento_personalizado)
print(f"Monto total: ${monto:.2f}")
print(f"Descuento aplicado ({descuento_personalizado}%): ${descuento2:.2f}")
print(f"Total a pagar: ${monto - descuento2:.2f}")

