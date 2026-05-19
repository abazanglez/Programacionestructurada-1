def capturar_lecturas():
    lecturas = []
    print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---")
    for i in range(8):
        temperatura = float(input("Lectura " + str(i + 1) + ": "))
        lecturas.append(temperatura)
    return lecturas

def filtrar_lecturas(lecturas):
    contador_errores = 0
    for i in range(len(lecturas)):
        if lecturas[i] < 0 or lecturas[i] > 100:
            lecturas[i] = 35.0
            contador_errores += 1
    print("Se detectaron " + str(contador_errores) + " lecturas erroneas y fueron corregidas a 35.0.")
    return lecturas

def calcular_promedio(lecturas):
    suma = 0
    for temperatura in lecturas:
        suma += temperatura
    promedio = suma / 8
    return promedio

def mostrar_resultados(lecturas, promedio):
    print("Datos limpios: " + str(lecturas))
    print("Promedio de operacion: " + str(promedio) + "°C")
    if promedio > 75:
        print("ALERTA: Activando sistema de enfriamiento liquido.")
    else:
        print("Estado: Operacion normal.")

def main():
    lecturas = capturar_lecturas()
    lecturas = filtrar_lecturas(lecturas)
    promedio = calcular_promedio(lecturas)
    mostrar_resultados(lecturas, promedio)

if __name__ == "__main__":
    main()