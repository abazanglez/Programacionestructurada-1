def bienvenida():
    nombre_asistente = "UXVA"
    print(f"Bienvenido, soy {nombre_asistente}, tu asistente virtual")
    return nombre_asistente

def obtener_frase():
    frase = input("En qué puedo ayudarte hoy?: ").lower()
    return frase

def clasificar_intencion(frase):
    if "hola" in frase or "buenos días" in frase:
        print("Hola! Soy tu asistente Es un gusto saludarte")
    elif "clima" in frase or "temperatura" in frase:
        print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado")
    elif "hora" in frase or "tiempo" in frase:
        print("La hora actual del sistema es: 10:30 AM")
    else:
        print("Lo siento, todavía no entiendo ese comando. Podrías intentar con otra palabra?")

def despedida(nombre_asistente):
    print("Proceso finalizado Gracias por usar", nombre_asistente)

def main():
    nombre_asistente = bienvenida()
    frase = obtener_frase()
    clasificar_intencion(frase)
    despedida(nombre_asistente)

if __name__ == "__main__":
    main()