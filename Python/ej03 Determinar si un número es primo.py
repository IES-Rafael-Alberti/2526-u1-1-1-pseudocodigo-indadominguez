

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mostrar_resultado(num: int) -> str:
    if es_primo(num):
        print(f"El número {num} es Primo.")
    else:
        print(f"El número {num} no es Primo.")

def main():
    num = pedir_numero("Introduce un número entero: ")
    mostrar_resultado(num)

if __name__ == "__main__":
    main()
