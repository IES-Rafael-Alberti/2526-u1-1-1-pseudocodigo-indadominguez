

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, introduzca un número válido. ")
        numero = input(mensaje)
    return int(numero)

def calculo_importe(horas_trabajadas: int, coste_por_hora: int) -> int:

    return coste_por_hora * horas_trabajadas


def mostar_resultado(importe_total: int):
    print(f"El importe total es de: {importe_total}€")


def main():
    horas_trabajadas = pedir_numero(("Introduzca las horas trabajadas: "))
    coste_por_hora = pedir_numero(("Introduzca el coste por hora: "))
    importe_total = calculo_importe(horas_trabajadas, coste_por_hora)
    mostar_resultado(importe_total)

if __name__ == "__main__":
    main()