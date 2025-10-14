
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)


def calculo_peso(payasos: int, muñecos: int):
    peso_payasos = 112
    peso_muñecos = 75
    resultado = payasos * peso_payasos + peso_muñecos * muñecos
    return resultado


def main():
    payasos = pedir_numero("Introduzca el número de payasos: ")
    muñecos = pedir_numero("Introduzca el número de muñecos: ")
    total = calculo_peso(payasos, muñecos)
    print(f"El peso total del paquete es: {total}")
    

if __name__ == "__main__":
    main()