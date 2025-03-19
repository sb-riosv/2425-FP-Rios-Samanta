def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y el monto final después del descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Tupla con el monto del descuento y el total a pagar.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final


# Llamadas a la función
monto1 = 1200  # Ejemplo de compra de 1200 dólares
descuento1, total1 = calcular_descuento(monto1)
print(f"Compra de ${monto1}: Descuento aplicado: ${descuento1:.2f}, Total a pagar: ${total1:.2f}")

monto2 = 5000  # Ejemplo de compra de 1500 dólares con 15% de descuento
porcentaje2 = 15
descuento2, total2 = calcular_descuento(monto2, porcentaje2)
print(f"Compra de ${monto2} con {porcentaje2}% de descuento: Descuento aplicado: ${descuento2:.2f}, Total a pagar: ${total2:.2f}")
