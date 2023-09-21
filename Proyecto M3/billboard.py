# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:35:48 2023

@author: USUARIO
"""
# billboard.py

def cargar_canciones(nombre_archivo):
    """Carga canciones desde un archivo CSV y las retorna como una lista de diccionarios."""
    canciones = []
    # Aquí debes implementar la lectura del archivo CSV y la creación de los diccionarios.
    # Puedes utilizar la librería csv de Python para esto.
    # Asume que el archivo CSV tiene columnas: posicion, nombre_cancion, nombre_artista, anio, letra
    # Agrega cada canción como un diccionario a la lista "canciones".
    
    # Ejemplo de cómo agregar una canción a la lista:
    cancion = {
        'posicion': 1,
        'nombre_cancion': 'Canción 1',
        'nombre_artista': 'Artista 1',
        'anio': 2022,
        'letra': 'Letra de la canción 1'
    }
    canciones.append(cancion)
    
    return canciones

def buscar_cancion(canciones, nombre, anio):
    """Busca una canción por nombre y año y retorna su información en un diccionario."""
    for cancion in canciones:
        if cancion['nombre_cancion'] == nombre and cancion['anio'] == int(anio):
            return cancion
    return None

def canciones_anio(canciones, anio):
    """Retorna una lista de diccionarios con las canciones de un año dado."""
    canciones_del_anio = []
    for cancion in canciones:
        if cancion['anio'] == int(anio):
            cancion_sin_letra = cancion.copy()
            del cancion_sin_letra['letra']
            canciones_del_anio.append(cancion_sin_letra)
    return canciones_del_anio

# Implementa las demás funciones de acuerdo a las instrucciones.

# ...

def promedio_canciones_por_artista(canciones):
    """Retorna la cantidad promedio de canciones por artista."""
    artistas = set()
    canciones_totales = 0
    
    for cancion in canciones:
        nombre_artista = cancion['nombre_artista']
        if nombre_artista not in artistas:
            artistas.add(nombre_artista)
            canciones_totales += 1
    
    if not artistas:
        return 0
    
    return canciones_totales / len(artistas)
