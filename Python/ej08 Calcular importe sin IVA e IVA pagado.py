

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)


def calcular_iva(precio_final: int) -> tuple:

    IVA = 10
    precio_sin_iva = precio_final / (1 + IVA / 100)

    iva_pagado = precio_final - precio_sin_iva

    return precio_sin_iva, iva_pagado


def mostrar_resultado(precio_sin_iva: float, iva_pagado: float):
    print(f"El precio sin iva es {precio_sin_iva:.2f} ")
    print(f"El iva pagado es {iva_pagado:.2f} ")
    

def main():
    precio_final = pedir_numero("Introduzca el precio final del artículo: ")
    precio_sin_iva, iva_pagado = calcular_iva(precio_final)
    mostrar_resultado(precio_sin_iva, iva_pagado)


if __name__ == "__main__":
    main()