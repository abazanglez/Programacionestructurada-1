class MonitorEntrenamiento:
    def __init__(self):
        self.historial_errores = []
        self.umbral_convergencia = 0.01

    def registrar_epoca(self, valor_error):
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzo el objetivo de precision.")
        self.historial_errores.append(valor_error)

def main():
    monitor = MonitorEntrenamiento()
    print("--- Iniciando Monitor de Red Neuronal ---")

    epoca = 1
    while epoca <= 5:
        entrada = input("Ingrese el error de la Epoca " + str(epoca) + ": ")
        try:
            valor = float(entrada)
            if valor < 0:
                print("> [ERROR] El error no puede ser un numero negativo.")
            else:
                monitor.registrar_epoca(valor)
                print("> Registro exitoso.")
                epoca += 1
        except ValueError:
            print("> [ERROR] Entrada invalida. Por favor, ingrese un numero decimal.")

    print("\n--- Resumen de Entrenamiento ---")
    print("Historial:", monitor.historial_errores)
    promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
    print("Promedio de Error:", promedio)
    print("Mejor resultado obtenido:", min(monitor.historial_errores))

if __name__ == "__main__":
    main()