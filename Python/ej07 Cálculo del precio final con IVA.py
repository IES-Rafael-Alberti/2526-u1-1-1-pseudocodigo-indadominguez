
"""
Ejercicio precio con iva

Introduce los valores correctos dentro de la función pedir_numero y realiza la operación para 
calular el valor del artículo sin iva + el iva correspondiente dando el resultado en la función mostrar_resultado 
dentro del main

"""

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)

def calcular_precio_final(precio: int, iva: int) -> float:
    return precio + (precio * iva / 100)

def mostrar_resultado(total: float):
    print(f"El precio final con IVA es: {total:.2f} €")

def main():
    precio = pedir_numero("Introduzca el precio del artículo sin IVA: ")
    iva = pedir_numero("Introduzca el porcentaje de IVA: ")
    total = calcular_precio_final(precio, iva)
    mostrar_resultado(total)

if __name__ == "__main__":
    main()




