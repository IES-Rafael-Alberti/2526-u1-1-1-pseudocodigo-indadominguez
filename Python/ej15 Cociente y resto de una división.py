

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)


def calculo(num1: int, num2: int) -> None:
    if num2 != 0:
        cociente = num1 // num2
        resto = num1 % num2
        print(f"El cociente de la operación es: {cociente}")
        print(f"El resto de la operación es: {resto}")
    else:
        print("ERROR!!! No se puede dividir entre 0.")

def main():
    num1 = pedir_numero("Introduzca el dividendo de la operación: ")
    num2 = pedir_numero("Introduca el divisor de la operación: ")
    calculo(num1, num2)



if __name__ == "__main__":
    main()