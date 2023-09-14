# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 07:41:49 2023

@author: Ing. Leon
"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la película."""
    print("Nombre:", pelicula["nombre"])
    print("Género:", pelicula["genero"])
    print("Duración:", pelicula["duracion"], "mins")
    print("Año:", pelicula["anio"])
    print("Clasificación:", pelicula["clasificacion"])
    print("Hora:", f'{pelicula["hora"] // 100:02}:{pelicula["hora"] % 100:02}')
    print("Día:", pelicula["dia"])

def consultar_pelicula_mas_larga(peliculas: list) -> dict:
    """Encuentra la película más larga en una lista de películas."""
    pelicula_mas_larga = None
    duracion_mas_larga = 0

    for pelicula in peliculas:
        if pelicula["duracion"] > duracion_mas_larga:
            duracion_mas_larga = pelicula["duracion"]
            pelicula_mas_larga = pelicula

    return pelicula_mas_larga

def consultar_duracion_promedio_peliculas(peliculas: list) -> float:
    """Calcula la duración promedio de las películas en una lista."""
    total_duracion = sum(pelicula["duracion"] for pelicula in peliculas)
    return total_duracion / len(peliculas) if peliculas else 0

def consultar_peliculas_de_estreno(peliculas: list, anio_estreno: int) -> list:
    """Encuentra las películas de estreno en una lista."""
    return [pelicula for pelicula in peliculas if pelicula["anio"] > anio_estreno]

def contar_peliculas_clasificacion_18_mas(peliculas: list) -> int:
    """Cuenta cuántas películas tienen clasificación 18+ en una lista."""
    return len([pelicula for pelicula in peliculas if pelicula["clasificacion"] == "18+"])

def reagendar_pelicula(peliculas: list, nombre_pelicula: str, nuevo_dia: str) -> bool:
    """Reagenda una película en la lista según el nombre de la película y el nuevo día."""
    for pelicula in peliculas:
        if pelicula["nombre"].lower() == nombre_pelicula.lower():
            pelicula["dia"] = nuevo_dia
            return True
    return False

def decidir_invitar_a_ver_pelicula(peliculas: list, nombre_pelicula: str) -> str:
    """Decide si se puede invitar a alguien a ver una película según su nombre."""
    for pelicula in peliculas:
        if pelicula["nombre"].lower() == nombre_pelicula.lower():
            if pelicula["clasificacion"] == "18+":
                return "No puedes invitar a menores a ver esta película."
            else:
                return "Puedes invitar a ver esta película."
    return "No se encontró ninguna película con ese nombre."

def iniciar_aplicacion():
    peliculas = [
        mod.crear_pelicula("Shrek", "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes"),
        mod.crear_pelicula("Get Out", "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado"),
        mod.crear_pelicula("Icarus", "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo"),
        mod.crear_pelicula("Inception", "Acción, Drama", 148, 2010, '13+', 1300, "Lunes"),
        mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")
    ]

    while True:
        print("\nMi agenda de películas para la semana de receso")
        print("-" * 50)
        for idx, pelicula in enumerate(peliculas, start=1):
            print(f"Película {idx}")
            mostrar_informacion_pelicula(pelicula)
            print("-" * 50)

        print("\nMenu de opciones")
        print("1 - Consultar película más larga")
        print("2 - Consultar duración promedio de las películas")
        print("3 - Consultar películas de estreno")
        print("4 - Consultar cuántas películas tienen clasificación 18+")
        print("5 - Reagendar película")
        print("6 - Decidir si se puede invitar a alguien")
        print("7 - Salir de la aplicación")

        opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

        if opcion_elegida == "1":
            pelicula_mas_larga = consultar_pelicula_mas_larga(peliculas)
            if pelicula_mas_larga:
                print("\nLa película más larga es:")
                mostrar_informacion_pelicula(pelicula_mas_larga)
            else:
                print("\nNo se encontró ninguna película en la lista.")
        elif opcion_elegida == "2":
            duracion_promedio = consultar_duracion_promedio_peliculas(peliculas)
            print(f"\nLa duración promedio de las películas es: {duracion_promedio:.2f} minutos")
        elif opcion_elegida == "3":
            anio_estreno = int(input("\nIngrese el año de estreno para encontrar películas de estreno: "))
            peliculas_estreno = consultar_peliculas_de_estreno(peliculas, anio_estreno)
            if peliculas_estreno:
                print("\nPelículas de estreno:")
                for pelicula in peliculas_estreno:
                    mostrar_informacion_pelicula(pelicula)
            else:
                print("\nNo se encontraron películas de estreno para el año especificado.")
        elif opcion_elegida == "4":
            peliculas_18_mas = contar_peliculas_clasificacion_18_mas(peliculas)
            print(f"\nHay {peliculas_18_mas} películas con clasificación 18+ en la lista.")
        elif opcion_elegida == "5":
            nombre_pelicula = input("\nIngrese el nombre de la película que desea reagendar: ")
            nuevo_dia = input("Ingrese el nuevo día para la película: ")
            if reagendar_pelicula(peliculas, nombre_pelicula, nuevo_dia):
                print(f"\nLa película {nombre_pelicula} ha sido reagendada para el día {nuevo_dia}.")
            else:
                print("\nNo se encontró ninguna película con ese nombre en la lista.")
        elif opcion_elegida == "6":
            nombre_pelicula = input("\nIngrese el nombre de la película que desea verificar si se puede invitar: ")
            resultado = decidir_invitar_a_ver_pelicula(peliculas, nombre_pelicula)
            print("\n" + resultado)
        elif opcion_elegida == "7":
            print("\nSaliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("\nLa opción ingresada no es válida. Por favor, elija una opción del menú.")

if __name__ == "__main__":
    iniciar_aplicacion()

