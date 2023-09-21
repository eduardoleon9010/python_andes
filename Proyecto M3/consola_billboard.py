# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:31:09 2023

@author: USUARIO
"""

# consola_billboard.py
import billboard as bb  # Importa tu módulo billboard.py

def ejecutar_cargar_canciones():
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de las canciones y las carga."""
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.cargar_canciones(archivo)
    
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")

def ejecutar_buscar_cancion(canciones):
    """Ejecuta la opción de buscar una canción dado el nombre y el año del ranking al cual pertenece."""
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = input("Por favor ingrese el año de la canción que desea buscar: ")
    
    resultado = bb.buscar_cancion(canciones, cancion, anio)
    
    if resultado is None:
        print("Canción no encontrada")
    else:
        print(resultado)

def ejecutar_canciones_anio(canciones):
    """Ejecuta la opción de consultar las canciones de un año dado."""
    anio = input("Por favor ingrese el año que desea consultar: ")
    
    resultado = bb.canciones_anio(canciones, anio)
    
    if not resultado:
        print("No hay ninguna canción en ese año:", resultado)
    else:
        for cancion in resultado:
            print(cancion)

# Continúa con las demás funciones de ejecución, manteniendo la estructura optimizada.

# ...

def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario."""
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")    
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    canciones = []
    
    while True:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        
        if opcion_seleccionada == 1:
            ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 11:
            break
        else:
            print("Por favor seleccione una opción válida.")

if __name__ == "__main__":
    iniciar_aplicacion()
