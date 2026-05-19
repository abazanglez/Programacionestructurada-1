import math
import datetime

def imprimir_encabezado():
    fecha = datetime.date.today()
    print("================================")
    print("   Sistema de Salud Inteligente")
    print("   Fecha:", fecha)
    print("================================")

def calcular_imc(peso, estatura):
    resultado = peso / (estatura ** 2)
    return resultado

def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

def main():
    imprimir_encabezado()

    nombre = input("Nombre del paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (metros): "))
    presion = float(input("Presion sistolica: "))

    imc = calcular_imc(peso, estatura)
    estado_presion = evaluar_presion(presion)

    print("\n--- Resumen del Paciente ---")
    print("Paciente:", nombre)
    print("IMC:", math.ceil(imc))
    print("Estado de presion:", estado_presion)

if __name__ == "__main__":
    main()