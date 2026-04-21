def imprimir_tabla(filas=4, columnas=15):
    # Encabezado
    print("   ", end="")
    for j in range(1, columnas + 1):
        print(f"{j:4}", end="")
    print()

    # Línea separadora
    print("   " + "----" * columnas)

    # Filas
    for i in range(1, filas + 1):
        print(f"{i}* ", end="")
        for j in range(1, columnas + 1):
            print(f"{i*j:4}", end="")
        print()


def main():
    imprimir_tabla()


if __name__ == "__main__":
    main()