


def main():
    palabra = input("Intrpduce una palabra: ")
    palabra_invertida = ""

    for i in range(len(palabra)-1, -1, -1):
        palabra_invertida += palabra[i]


    print(f"La palabra invertida es: {palabra_invertida}")



if __name__ == "__main__":
    main()