#desarrollo de algoritmo contador de positivos 

def contador_positivos():
    cotador=0
    while True:
        numero = int(input("Ingrese un numero(0 para terminar):"))
        if numero <0:
            break
        contador +=1


    print("Cantidad de numeros positivos integrados:", contador) 


#definicion de la funcion main (controla el flujo del programa)

def main():
    print("Bienveido al contador de positivos")
    contador_positivos()


    #llamada a la funcion main para iniciar el programa
    if __name__ == "__main__":
        main()