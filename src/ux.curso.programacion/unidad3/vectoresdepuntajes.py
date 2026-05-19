def inicializar_vector():
    puntajes_sentimiento = [0, 0, 0]
    return puntajes_sentimiento

def capturar_palabras(puntajes_sentimiento):
    print("--- ANALIZADOR DE SENTIMIENTOS IA ---")
    for i in range(5):
        opcion = int(input("Palabra " + str(i + 1) + " - Clasificacion (0, 1, 2): "))
        puntajes_sentimiento[opcion] += 1
    return puntajes_sentimiento

def encontrar_maximo(puntajes_sentimiento):
    maximo = puntajes_sentimiento[0]
    indice_maximo = 0
    for i in range(len(puntajes_sentimiento)):
        if puntajes_sentimiento[i] > maximo:
            maximo = puntajes_sentimiento[i]
            indice_maximo = i
    return indice_maximo

def mostrar_resultado(puntajes_sentimiento, indice_maximo):
    print("\nEstado final del vector de caracteristicas: " + str(puntajes_sentimiento))
    if indice_maximo == 0:
        print("Resultado de IA: La frase es Positiva (Predominancia en indice 0)")
    elif indice_maximo == 1:
        print("Resultado de IA: La frase es Neutral (Predominancia en indice 1)")
    elif indice_maximo == 2:
        print("Resultado de IA: La frase es Negativa (Predominancia en indice 2)")

def main():
    puntajes_sentimiento = inicializar_vector()
    puntajes_sentimiento = capturar_palabras(puntajes_sentimiento)
    indice_maximo = encontrar_maximo(puntajes_sentimiento)
    mostrar_resultado(puntajes_sentimiento, indice_maximo)

if __name__ == "__main__":
    main()