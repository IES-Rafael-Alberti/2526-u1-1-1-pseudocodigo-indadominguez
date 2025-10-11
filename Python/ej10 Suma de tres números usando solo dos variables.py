
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)

def sumar_numero() -> int:
    suma = 0
    for i in range(1,4):
        numero = pedir_numero(f"Introduzca el número {i}: ")
        suma += numero
    return suma

def mostrar_resultado(resultado: int):
    print(f"La suma de los tres numero es: {resultado}")

def main():
   resultado = sumar_numero()
   mostrar_resultado(resultado)





if __name__ == "__main__":
    main()