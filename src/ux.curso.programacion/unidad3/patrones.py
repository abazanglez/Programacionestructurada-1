def configurar_patron():
    patron_maestro = [1, 0, 1, 1, 0]
    return patron_maestro

def capturar_lectura():
    lectura_sensor = []
    print("--- ESCANER BIOMETRICO DE IA ---")
    for i in range(5):
        valor = int(input("Ingrese bit " + str(i + 1) + ": "))
        lectura_sensor.append(valor)
    return lectura_sensor

def comparar_vectores(patron_maestro, lectura_sensor):
    coincidencias = 0
    for i in range(5):
        if patron_maestro[i] == lectura_sensor[i]:
            coincidencias += 1
    return coincidencias

def calcular_similitud(coincidencias):
    similitud = (coincidencias / 5) * 100
    return similitud

def tomar_decision(similitud):
    if similitud == 100:
        print("ESTADO: ACCESO TOTAL: Identidad Verificada.")
    elif similitud >= 60 and similitud <= 99:
        print("ESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificacion manual.")
    else:
        print("ESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")

def mostrar_comparacion(patron_maestro, lectura_sensor):
    print("Patron maestro: " + str(patron_maestro))
    print("Lectura sensor: " + str(lectura_sensor))

def main():
    patron_maestro = configurar_patron()
    lectura_sensor = capturar_lectura()

    print("\n> Comparando lectura con base de datos...")
    coincidencias = comparar_vectores(patron_maestro, lectura_sensor)
    similitud = calcular_similitud(coincidencias)

    print("> Coincidencias encontradas: " + str(coincidencias))
    print("> Porcentaje de Similitud: " + str(similitud) + "%")
    tomar_decision(similitud)
    mostrar_comparacion(patron_maestro, lectura_sensor)

if __name__ == "__main__":
    main()