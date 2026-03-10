from faker import Faker 
faker = Faker ("es_MX")

ciudades_ia = []

#2. Operacion de llenados(ciclo)
for _ in range(5):
    ciudades_ia.append(faker.city())


    #3. Eacritura de arreglos (mostrar resultados)
    print("/n--DATATEST DE CIUDADES GENERADO--")
    for i in range (len(ciudades_ia)):
      print(f"Registro{i+1}:{ciudades_ia[i]}")
       