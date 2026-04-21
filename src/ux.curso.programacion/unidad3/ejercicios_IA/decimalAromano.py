TABLA_ROMANA = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]


def leer_numero():
    n = int(input("Ingresa un número entero (1 - 3000): "))
    return n


def validar_rango(n):
    return 1 <= n <= 3000


def decimal_a_romano(n):
    resultado = ""
    for valor, simbolo in TABLA_ROMANA:
        while n >= valor:
            resultado += simbolo
            n -= valor
    return resultado


def mostrar_resultado(n_original, romano):
    print(f"\n{n_original} en notación romana es: {romano}")


def main():
    n = leer_numero()
    if not validar_rango(n):
        print("Error: el número debe estar entre 1 y 3000")
        return
    romano = decimal_a_romano(n)
    mostrar_resultado(n, romano)


if __name__ == "__main__":
    main()