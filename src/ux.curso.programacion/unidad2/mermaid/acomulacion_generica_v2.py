
#acomulacio generica

def acomulacion():
    suma=0
    while True:
        numero=int(input("Ingrese un numero: "))
        if numero>=10 and numero<=50:
            suma+=numero
        else:
            break
    return suma


def main():
    resultado = acomulacion()
    print("La suma acomulada es: ", resultado)

if __name__ == "__main__":
    main()

