

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)

def cambio_temperatura(celsius: int) -> float:
    return (celsius * 9 / 5 ) + 32

def mostrar_resultado(total: float):
    print(f"La temperatura es {total:.2f} grados fahrenheit")

def main():
    celsius = pedir_numero("Introduzca los grados en Celsius: ")
    total = cambio_temperatura(celsius)
    mostrar_resultado(total)

if __name__ == "__main__":
    main()
