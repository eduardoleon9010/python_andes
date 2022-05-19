# -*- coding: utf-8 -*-
def mas_a (c1: str, c2: str, c3: str, c4: str)-> str:
    letra = 'a'
    cadena_mas = c1
    cantidad_mas = c1.lower().count(letra)


    if c2.lower().count(letra) > cantidad_mas:
        cadena_mas = c2
        cantidad_mas = c2.lower().count(letra)
    if c3.lower().count(letra) > cantidad_mas:
        cadena_mas = c3
        cantidad_mas = c3.lower().count(letra)
    if c4.lower().count(letra) > cantidad_mas:
        cadena_mas = c4
        cantidad_mas = c4.lower().count(letra)
        
    return cadena_mas