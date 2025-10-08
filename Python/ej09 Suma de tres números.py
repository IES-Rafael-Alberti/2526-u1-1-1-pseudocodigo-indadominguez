

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)


def suma(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


def mostrar_resultado(resultado: int):
    print(f"La suma es: {resultado}")


def main():
    num1 = pedir_numero("Introduzca un número entero positivo:")
    num2 = pedir_numero("Introduzca un número entero positivo:")
    num3 = pedir_numero("Introduzca un número entero positivo:")
    
    resultado = suma(num1, num2, num3)
    mostrar_resultado(resultado)

if __name__ == "__main__":
    main()