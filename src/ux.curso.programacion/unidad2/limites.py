def declarar_constantes():
    LIMITE_SUPERIOR = 100.0
    LIMITE_INFERIOR = 0.0
    return LIMITE_SUPERIOR, LIMITE_INFERIOR

def obtener_lectura():
    lectura = float(input("Ingrese la lectura del sensor térmico: "))
    return lectura

def validar_y_procesar(lectura, LIMITE_INFERIOR, LIMITE_SUPERIOR):
    if lectura >= LIMITE_INFERIOR and lectura <= LIMITE_SUPERIOR:
        dato_normalizado = lectura / LIMITE_SUPERIOR
        print("Señal aceptada Valor normalizado para el modelo:", dato_normalizado)
    else:
        print("Error: Lectura fuera de rango La señal se considera ruido")

def salida_final():
    print("Fin del proceso de filtrado de datos")

def main():
    LIMITE_SUPERIOR, LIMITE_INFERIOR = declarar_constantes()
    lectura = obtener_lectura()
    validar_y_procesar(lectura, LIMITE_INFERIOR, LIMITE_SUPERIOR)
    salida_final()

if __name__ == "__main__":
    main()