peliculas_accion = ["Mad Max", "John Wick", "Inception"]
peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
peliculas_terror = ["It", "The Conjuring", "Saw"]

def obtener_recomendacion(genero_elegido, edad_usuario):
    if edad_usuario < 13:
        return peliculas_comedia[0]
    else:
        if genero_elegido == "accion":
            return peliculas_accion[0]
        elif genero_elegido == "comedia":
            return peliculas_comedia[0]
        elif genero_elegido == "terror":
            return peliculas_terror[0]

def main():
    print("Agente IA de Recomendacion activo. Bienvenido.")

    edad = int(input("Ingresa tu edad: "))
    genero = input("Ingresa tu genero favorito (accion, comedia, terror): ")

    if edad < 13 and genero == "terror":
        print("Nota: Debido a tu edad, hemos ajustado la recomendacion a contenido apto para todo publico.")

    pelicula = obtener_recomendacion(genero, edad)
    print("Recomendacion de la IA: " + pelicula)

if __name__ == "__main__":
    main()