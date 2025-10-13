
def pedir_nombre(mensaje: str) ->str:
    nombre = input(mensaje)
    return nombre



def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)


def repeticion_nombre(nombre: str, numero: int) -> str:
    resultado = ""
    for i in range(numero):
        resultado += nombre + "\n"
    return resultado


def main():
    nombre_usuario = pedir_nombre("Introduzca su nombre: ")
    nombre_repite = pedir_numero("Introduzca el número de veces que se repite el nombre: ")
    resultado = repeticion_nombre(nombre_usuario, nombre_repite)
    print(resultado)


if __name__ == "__main__":
    main()