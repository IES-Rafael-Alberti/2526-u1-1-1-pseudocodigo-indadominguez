


def calcular_saldos(salario_inicial: float):
    interes = 0.04
    saldo_año1 = salario_inicial * (1 + interes)
    saldo_año2 = saldo_año1 * (1 + interes)
    saldo_año3 = saldo_año2 * (1 + interes)

    print(f"Su saldo el primer año es: {saldo_año1}")
    print(f"Su saldo el segundo añs es: {saldo_año2}")
    print(f"Su saldo el tercer año es: {saldo_año3} ")

def main():
    salario = float(input("Introduca su salario anual: "))
    calcular_saldos(salario)



if __name__ == "__main__":
    main()