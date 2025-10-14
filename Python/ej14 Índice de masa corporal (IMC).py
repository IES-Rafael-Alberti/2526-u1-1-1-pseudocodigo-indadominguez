
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)


def imc(peso: int, altura: float) -> float:
    resultado = peso / (altura * altura)
    return resultado


def main():
    peso = pedir_numero("Introduzca su peso en kilogramos: ")
    altura_cm = pedir_numero("Introduzca su altura en centímetros: ")
    altura_m = altura_cm / 100  

    resultado = imc(peso, altura_m)
    print(f"Su IMC es: {resultado}")


if __name__ == "__main__":
    main()
