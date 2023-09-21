# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 07:16:47 2023

@author: Ing. Leon
"""

import modulos_peliculas as mod

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
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
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    if pelicula_mas_larga:
        print("Película más larga:")
        mod.mostrar_informacion_pelicula(pelicula_mas_larga)
    else:
        print("No hay películas en la agenda.")

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    duracion_promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print(f"Duración promedio de las películas: {duracion_promedio}")

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """ Ejecuta la opcion de buscar películas de estreno. Esto es: las películas que sean 
        más recientes que un año dado.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    anio = int(input("Ingrese el año límite para buscar películas de estreno: "))
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    
    if estrenos:
        print(f"Películas de estreno desde {anio}:")
        print(estrenos)
    else:
        print(f"No se encontraron películas de estreno desde {anio}.")

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Indica cuántas películas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    cantidad_18_mas = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print(f"Cantidad de películas con clasificación '18+': {cantidad_18_mas}")

def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de reagendar una película.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una película de la agenda")

    nombre = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        nueva_hora = int(input("Ingrese la nueva hora (en formato HHMM): "))
        nuevo_dia = input("Ingrese el nuevo día: ")
        control_horario = input("¿Desea aplicar control horario? (S/N): ").strip().lower() == "s"

        if mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5):
            print("La película se ha reagendado con éxito.")
        else:
            print("No se pudo reagendar la película debido a conflictos de horario.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una película o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Decidir si se puede invitar a alguien a ver una película")

    nom_peli = input("Ingrese el nombre de la película: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        edad_invitado = int(input("Ingrese la edad del invitado: "))
        autorizacion_padres = input("¿Tiene autorización de sus padres? (S/N): ").strip().lower() == "s"

        if mod.decidir_invitar(pelicula, edad_invitado, autorizacion_padres):
            print("Puede invitar al invitado a ver la película.")
        else:
            print("No puede invitar al invitado a ver la película debido a restricciones de edad o autorización.")


