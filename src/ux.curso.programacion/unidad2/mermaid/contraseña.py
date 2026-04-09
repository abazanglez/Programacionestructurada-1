def login():
   
    intentos = 0
    clave_correcta = "1234"

   
    while intentos < 3:
      
        contrasena = input("Ingrese la contraseña: ")

      
        if contrasena == clave_correcta:
            print("Acceso Concedido")
            break
        else:
            intentos += 1
            print("Contraseña incorrecta")

   
    if intentos == 3:
        print("Cuenta bloqueada")


def main():
    login()


if __name__ == "__main__":
    main()