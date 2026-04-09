def acumulacion():
    
    total_acumulado = 0
    semanas = 0
    meta = 2500

   
    while total_acumulado < meta:
       
        salario_semanal = float(input("Ingresa el salario de la semana: "))
        
        
        total_acumulado = total_acumulado + salario_semanal
        semanas = semanas + 1

    
    return semanas


def main():
    resultado = acumulacion()
    
   
    print("Semanas trabajadas:", resultado)


if __name__ == "__main__":
    main()