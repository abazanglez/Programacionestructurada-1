def enteros():
    dividendo = int(input("Ingresa el dividendo (A): "))
    divisor   = int(input("Ingresa el divisor  (B): "))
    return dividendo, divisor


def entera(dividendo, divisor):
    if divisor == 0:
        return None, None

    cociente = 0
    resto    = dividendo

    while resto >= divisor:
        resto    = resto - divisor
        cociente = cociente + 1

    return cociente, resto


def mostrar_resultado(dividendo, divisor, cociente, resto):
    if cociente is None:
        print("Error: el divisor no puede ser 0.")
    else:
        print(f"\n{dividendo} ÷ {divisor}")
        print(f"  Cociente : {cociente}")
        print(f"  Resto    : {resto}")
        print(f"  Prueba   : {divisor} × {cociente} + {resto} = {divisor * cociente + resto}")


def main():
    dividendo, divisor       = enteros()
    cociente,  resto         = division_entera(dividendo, divisor)
    mostrar_resultado(dividendo, divisor, cociente, resto)


if __name__ == "__main__":
    main()