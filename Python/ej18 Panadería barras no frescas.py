def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)


def calculo_barras(barras: int):
    precio_barra = 3.49
    descuento = 0.6

    precio_descuento = precio_barra * (1 - descuento)
    coste_total = barras * precio_descuento
    descuento_total = barras * precio_barra * descuento

    return coste_total, descuento_total, precio_barra, precio_descuento


def mostrar_resultado(barras: int, precio_barra: float, precio_descuento: float, coste_total: float, descuento_total: float):
    print(f"Precio habitual por barra: {precio_barra:.2f} €")
    print(f"Precio con descuento por barra: {precio_descuento:.2f} €")
    print(f"Coste total por {barras} barras: {coste_total:.2f} €")
    print(f"Descuento total aplicado: {descuento_total:.2f} €")


def main():
    numero_barras = pedir_numero("Introduzca el número de barras que necesita: ")
    coste_total, descuento_total, precio_barra, precio_descuento = calculo_barras(numero_barras)
    mostrar_resultado(numero_barras, precio_barra, precio_descuento, coste_total, descuento_total)


if __name__ == "__main__":
    main()
