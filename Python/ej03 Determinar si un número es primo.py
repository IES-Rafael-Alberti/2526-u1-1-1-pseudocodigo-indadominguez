
numero = int(input("Introduce un número entero: "))

def es_primo(n):
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0: 
            return False
    return True

if es_primo(numero):
    print(f"El número {numero} es Primo. ")

else:
    print(f"El número {numero} no es Primo. ")
