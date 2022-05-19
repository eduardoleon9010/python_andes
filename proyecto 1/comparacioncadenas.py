# -*- coding: utf-8 -*-
def comparar_cadenas(palabra1: str, palabra2: str,)->None:
    if (palabra1 == palabra2):
        print("Las palabras son uguales")
    elif (palabra1 < palabra2):
        print("Las palabras",palabra1,"es meneos quela palabra",palabra2)
    else:
        print("La palabra",palabra1,"es mayor que la palabra",palabra2)