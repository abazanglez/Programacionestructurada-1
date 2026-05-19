class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print("[ACCESO CONCEDIDO] Bienvenido, rol detectado: " + rol + ".")
            if rol == "Administrador":
                agregar = input("¿Desea agregar un nuevo usuario? (si/no): ")
                if agregar == "si":
                    nueva_matricula = input("Nueva matricula: ")
                    nuevo_rol = input("Rol del nuevo usuario: ")
                    self.usuarios_autorizados[nueva_matricula] = nuevo_rol
                    print("Usuario agregado correctamente.")
        else:
            print("[ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")

def main():
    sistema = ControlAcceso()
    print("--- Sistema de Seguridad Laboratorio IA - UX ---")

    while True:
        try:
            matricula = input("\nIngrese su matricula (o 'salir' para terminar): ")
            if matricula == "salir":
                break
            if matricula == "":
                raise ValueError
            sistema.verificar_permisos(matricula)
        except ValueError:
            print("[ERROR] El campo de matricula no puede estar vacio.")
        finally:
            print("--- Intento de acceso registrado en el log del servidor ---")

if __name__ == "__main__":
    main()