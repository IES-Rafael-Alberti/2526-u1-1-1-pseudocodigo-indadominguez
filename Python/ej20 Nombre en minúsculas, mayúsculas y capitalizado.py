def pedir_nombre(mensaje: str) -> str:
    nombre = input(mensaje)
    return nombre


def mostrar_variantes(nombre: str) -> str:
    minusculas = nombre.lower()
    mayusculas = nombre.upper()
    capitalizado = nombre.title()
    
    resultado = (
        f"Nombre en minúsculas: {minusculas}\n"
        f"Nombre en mayúsculas: {mayusculas}\n"
        f"Nombre con mayúsculas iniciales: {capitalizado}"
    )
    return resultado


def main():
    nombre_completo = pedir_nombre("Introduzca su nombre completo: ")
    resultado = mostrar_variantes(nombre_completo)
    print(resultado)


if __name__ == "__main__":
    main()
