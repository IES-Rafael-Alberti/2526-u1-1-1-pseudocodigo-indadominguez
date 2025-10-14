
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)


def calculo(numero: int):
    if numero > 0:
        suma = numero * (numero + 1) // 2
        print(f"La suma de los {numero} primeros enteros positivos es: {suma}")
    else:
        print("El número debe de ser entero positivo")
        

def main():
    numero = pedir_numero("Introduzca un número entero: ")
    calculo(numero)
    


if __name__ == "__main__":
    main()