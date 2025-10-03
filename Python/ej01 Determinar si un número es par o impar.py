

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido.")
        numero = input(mensaje)
    return int(numero)


def calcular_primo(num: int) -> str:
    
    if num % 2 == 0:
        return(f"El número {num} es PAR. ")

    else: 
        return(f"El número {num} es IMPAR")

def mostrar_resultado(mensaje: str):
    print(mensaje)


def main():
    num = pedir_numero("Introduzca un número entero:")
    resultado = calcular_primo(num)
    mostrar_resultado(resultado)

if __name__ == "__main__":
    main()