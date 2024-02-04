# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:34:13 2024

@author: USUARIO
"""

import modulos_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la película."""
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print(f"Nombre: {nombre} - Año: {anio} - Duración: {duracion} mins")
    print(f"Genero: {genero} - Clasificación: {clasificacion}")
    
    hora_formato = str(hora // 100).zfill(2)
    min_formato = str(hora % 100).zfill(2)

    print(f"Día: {dia} Hora: {hora_formato}:{min_formato}")

def ejecutar_encontrar_pelicula_mas_larga(*peliculas: dict) -> None:
    """Ejecuta la opción de encontrar la película más larga."""
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(*peliculas)
    print(f"La película más larga es {pelicula_mas_larga['nombre']} con una duración de {pelicula_mas_larga['duracion']} minutos")

def ejecutar_consultar_duracion_promedio_peliculas(*peliculas: dict) -> None:
    """Ejecuta la opción de consultar la duración promedio de las películas."""
    duracion_promedio = mod.duracion_promedio_peliculas(*peliculas)
    print(f"Duración promedio de películas: {duracion_promedio}")

def ejecutar_encontrar_estrenos(*peliculas: dict) -> None:
    """Ejecuta la opción de buscar películas de estreno."""
    anio_referencia = int(input("¿Cuál año desea que sea la referencia?: "))
    estrenos = mod.encontrar_estrenos(anio_referencia, *peliculas)
    print(f"Películas de estreno encontradas: {estrenos}")

def ejecutar_cuantas_peliculas_18_mas(*peliculas: dict) -> None:
    """Ejecuta la opción de consultar cuántas películas tienen clasificación '18+'."""
    cantidad_18_mas = mod.cuantas_peliculas_18_mas(*peliculas)
    print(f"Existen {cantidad_18_mas} películas con clasificación '18+'.")

def ejecutar_reagendar_pelicula(*peliculas: dict) -> None:
    """Ejecuta la opción de reagendar una película."""
    print("Reagendar una película de la agenda")

    nombre_pelicula = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula_a_reagendar = mod.encontrar_pelicula(nombre_pelicula, *peliculas)
    
    if pelicula_a_reagendar is None:
        print("No hay ninguna película con este nombre")
    else:
        nuevo_dia = input("Digite el día: ")
        nueva_hora = int(input("Digite la nueva hora en formato militar: "))
        control_horario = input("¿Desea control de horario 'N' o 'S'?: ")
        
        if mod.reagendar_pelicula(pelicula_a_reagendar, nueva_hora, nuevo_dia, control_horario, *peliculas):
            print("La película fue reagendada con éxito.")
        else:
            print("No se puede reagendar la película debido a conflictos.")

def ejecutar_decidir_invitar(*peliculas: dict) -> None:
    """Ejecuta la opción de decidir si se puede invitar a alguien a ver una película o no."""
    print("Decidir si se puede invitar a alguien a ver una película")

    nombre_pelicula = input("Ingrese el nombre de la película: ")
    pelicula_a_invitar = mod.encontrar_pelicula(nombre_pelicula, *peliculas)
    
    if pelicula_a_invitar is None:
        print("No hay ninguna película con este nombre")
    else:
        edad_invitado = int(input("Ingrese la edad de la persona que desea invitar: "))
        autorizacion_padres = input("¿Tiene autorización de los padres? (Sí/No): ").lower() == "si"
        
        if mod.decidir_invitar(pelicula_a_invitar, edad_invitado, autorizacion_padres):
            print("Puede invitar a la persona a ver la película.")
        else:
            print("No puede invitar a la persona a ver la película debido a restricciones.")

def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola."""
    pelicula1 = mod.crear_pelicula("Shrek", "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out", "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus", "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception", "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de películas para la semana de receso" + "\n" + ("-" * 50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-" * 50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-" * 50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-" * 50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-" * 50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-" * 50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Muestra al usuario las opciones de ejecución disponibles."""
    print("Menu de opciones")
    print(" 1 - Consultar película más larga")
    print(" 2 - Consultar duración promedio de las películas")
    print(" 3 - Consultar películas de estreno")
    print(" 4 - Consultar cuántas películas tienen clasificación 18+")
    print(" 5 - Reagendar película")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print(f"La opción {opcion_elegida} no es una opción válida.")
    
    return continuar_ejecutando

if __name__ == "__main__":
    iniciar_aplicacion()