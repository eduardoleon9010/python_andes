# -*- coding: utf-8 -*-
def es_positivo(x: int)->bool:
    positivo = x > 0
    return positivo

def es_negativo(x: int)->bool:
    negativo = x < 0
    return negativo
    
def es_cero(x: int)->bool:
    positivo = es_positivo(x)
    negativo = es_negativo(x)
    return not positivo and not negativo
    
def ordenadas(antes: str, despues: str)->bool:
    """ 
    Revisa si dos cadenas en un diccionario están ordenadas lexicográficamente
    Parámetros:
        antes (str): una cadena que está antes que la otra en un diccionario
        despues (str): una cadena que está después que la otra en un diccionario
    Retorno:
        (bool): Indica si las cadenas estaban ordenadas.
                El resultado será verdadero si la cadena 'antes' tiene que ir 
                antes que la cadena 'despues' en orden lexicográfico.
                El resultado será falso de lo contrario.   
    """
    estan_ordenadas = antes < despues
    return estan_ordenadas
