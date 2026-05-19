def modulo_sensores():
    sensores_distancia = []

    print("--- MODULO DE SENSORES (VECTORES) ---")
    for i in range(5):
        distancia = float(input("Ingrese distancia sensor " + str(i + 1) + ": "))
        sensores_distancia.append(distancia)

    promedio = sum(sensores_distancia) / len(sensores_distancia)

    if promedio < 2.0:
        print("Promedio de proximidad: " + str(promedio) + "m. Aviso: Reduciendo velocidad global.")
    else:
        print("Promedio de proximidad: " + str(promedio) + "m. Estado: Seguro.")

    return sensores_distancia

def llenar_matriz():
    camara_ia = []

    print("\n--- MODULO DE VISION (MATRICES) ---")
    print("Llenando matriz de camara 3x3:")

    for fila in range(3):
        fila_actual = []
        for col in range(3):
            valor = int(input("Fila " + str(fila) + ", Col " + str(col) + " (Brillo 0-255): "))
            if valor > 255:
                valor = 255
            fila_actual.append(valor)
        camara_ia.append(fila_actual)

    return camara_ia

def imprimir_matriz(camara_ia):
    print("\nVisualizacion de la imagen capturada:")
    for fila in camara_ia:
        print(fila)

def analizar_brillo(camara_ia):
    puntos_brillantes = 0

    for fila in camara_ia:
        for pixel in fila:
            if pixel > 200:
                puntos_brillantes += 1

    print("\nResultado de Analisis IA:")
    print("Se detectaron " + str(puntos_brillantes) + " pixeles de alta intensidad.")

def main():
    modulo_sensores()
    camara_ia = llenar_matriz()
    imprimir_matriz(camara_ia)
    analizar_brillo(camara_ia)

if __name__ == "__main__":
    main()