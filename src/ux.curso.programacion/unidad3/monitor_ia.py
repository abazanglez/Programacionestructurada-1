def capturar_telemetria():
    print("TELEMETRIA DE CLUSTER IA ")
    temperatura = float(input("Temperatura actual (°C): "))
    memoria = int(input("Uso de Memoria VRAM (%): "))
    enfriamiento = input("¿Enfriamiento activo? (si/no): ").lower()
    return temperatura, memoria, enfriamiento

def validar_memoria(memoria):
    if memoria > 100 or memoria < 0:
        print("Error: Lectura de memoria fuera de rango (0-100%).")
        return False
    return True

def diagnosticar(temperatura, memoria, enfriamiento):
    if temperatura > 90 or memoria == 100:
        print("¡ALERTA CRITICA! Apagando servidores para evitar daños fisicos.")
    elif temperatura >= 75 and temperatura <= 90:
        if enfriamiento == "no":
            print("Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
        elif enfriamiento == "si":
            print("Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
    elif temperatura < 75 and memoria < 80:
        print("Sistema Estable: Entrenamiento en curso a maxima capacidad.")
        memoria_libre = 100 - memoria
        print("Memoria VRAM disponible para otro modelo: " + str(memoria_libre) + "%")

def main():
    temperatura, memoria, enfriamiento = capturar_telemetria()

    if validar_memoria(memoria) == False:
        return

    print("\n> Diagnostico: ", end="")
    diagnosticar(temperatura, memoria, enfriamiento)

if __name__ == "__main__":
    main()