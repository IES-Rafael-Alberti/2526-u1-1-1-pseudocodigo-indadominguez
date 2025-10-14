
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)



def main():
    print("La suma de los números es: ",
            pedir_numero("Introduzca el primer número: ") +
            pedir_numero("Introduzca el segundo número: ") +
            pedir_numero("Introduzca el tercer número: "))


if __name__ == "__main__":
    main()