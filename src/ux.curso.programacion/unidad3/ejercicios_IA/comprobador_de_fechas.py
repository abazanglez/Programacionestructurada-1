def fecha():
    dia = int(input("Ingresa el día : "))
    mes = int(input("Ingresa el mes : "))
    return dia, mes


def max_dias_mes(mes):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    else:
        return 28


def es_fecha_valida(dia, mes):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > max_dias_mes(mes):
        return False
    return True


def mostrar_resultado(dia, mes, valida):
    fecha = f"{dia:02d}/{mes:02d}"
    if valida:
        print(f"\nLa fecha {fecha} es VÁLIDA.")
    else:
        print(f"\nLa fecha {fecha} es INVÁLIDA.")


def main():
    dia, mes = fecha()
    valida   = es_fecha_valida(dia, mes)
    mostrar_resultado(dia, mes, valida)


if __name__ == "__main__":
    main()