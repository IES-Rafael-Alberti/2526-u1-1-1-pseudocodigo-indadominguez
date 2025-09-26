

ingresar_horas = input("Introduzca el número de horas: ")
while not ingresar_horas.isdigit():
    print("***ERROR***, introduzca solo números enteros.")
    ingresar_horas = input("Introduzca el número de horas: ")
ingresar_horas = int(ingresar_horas)

ingresar_tarifa = input("Introduzca la tarifa por hora: ")
while not ingresar_tarifa.isdigit():
    print("***ERROR***, introduzca solo números enteros.")
    ingresar_tarifa = input("Introduzca la tarifa por hora: ")
ingresar_tarifa = int(ingresar_tarifa)

salario = ingresar_horas * ingresar_tarifa
print(f"El salario es de {salario} €")

