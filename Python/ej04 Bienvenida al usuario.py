

def pedir_nombre() -> str:
    return input("Introduzca su nombre: ")

def mostrar_resultado(nombre: str):
    print(f"Hola {nombre}")


def main():
    nombre = pedir_nombre()
    mostrar_resultado(nombre)


if __name__ == "__main__":
    main()