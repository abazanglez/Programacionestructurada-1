def capturar_datos():
    print("SISTEMA DE CONTROL BIOMETRICO ")
    nombre = input("Nombre del Ingeniero: ")
    id_empleado = int(input("ID de Empleado: "))
    iris = input("¿El escaneo de Iris coincide? (si/no): ").lower()
    facial = input("¿El reconocimiento facial es > 95%? (si/no): ").lower()
    return nombre, id_empleado, iris, facial

def evaluar_acceso(nombre, id_empleado, iris, facial):
    if id_empleado <= 0:
        print("¡ALERTA DE SEGURIDAD! ID invalido detectado. Bloqueando accesos y notificando a la policia.")
    elif iris == "si" and facial == "si":
        if id_empleado < 100:
            print("Bienvenido, Ingeniero " + nombre + ". Acceso nivel SENIOR concedido a todas las areas.")
            print("Generando log de entrada para el usuario: " + str(id_empleado) + "...")
        elif id_empleado >= 100:
            print("Bienvenido, Ingeniero " + nombre + ". Acceso nivel JUNIOR concedido. Areas de servidores restringidas.")
            print("Generando log de entrada para el usuario: " + str(id_empleado) + "...")
    else:
        print("Error Biometrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

def main():
    nombre, id_empleado, iris, facial = capturar_datos()
    print("\n> Diagnostico: ", end="")
    evaluar_acceso(nombre, id_empleado, iris, facial)

if __name__ == "__main__":
    main()