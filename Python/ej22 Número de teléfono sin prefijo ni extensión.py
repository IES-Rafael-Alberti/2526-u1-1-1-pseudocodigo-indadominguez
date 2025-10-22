
def pedir_numero(mensaje: str) ->str:
    telefono = input(mensaje)
    return telefono


def extraer_numero_central(telefono: str) -> str:
    partes = telefono.split("-")
    if len(partes) == 3:
        numero_central = partes[1]
        return numero_central
    else:
        return("Formato incorrecto")


def main():
    telefono = pedir_numero("Introduca su numero de telefono con prefijo y extensión: ")
    numero_central = extraer_numero_central(telefono)
    print(f"Numero central de su teléfonoes: {numero_central}")





if __name__ == "__main__":
    main()