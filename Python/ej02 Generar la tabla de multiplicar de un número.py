

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)


def generar_tabla(num: int):

    for i in range (1, 11):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")


def mostrar_resultado(num: int):
    generar_tabla(num)

def main():
    num = pedir_numero("Introduce un número entero: ")
    mostrar_resultado(num)


if __name__ == "__main__":
    main()