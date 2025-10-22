

def pedir_nombre(mensaje: str) -> str:
    nombre = input(mensaje)
    return nombre


def contar_letras(nombre: str) -> int:
    
    contador = 0

    for letra in nombre:
        if letra != "":
            contador += 1
    return contador


def main():
    nombre = pedir_nombre("Introduzca su nombre por favor: ")
    cantidad_letra = contar_letras(nombre)
    print(f"Las letras de tu nombre son: {cantidad_letra}")



if __name__ == "__main__":
    main()