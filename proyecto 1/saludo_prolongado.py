# -*- coding: utf-8 -*-
def saludar_repetidas_veces(nombre: str, veces: int)->str:
    """ Saludo prolongado
    Parámetros:
      nombre (str): Nombre a incluir en el saludo
      veces (int): Cantidad de veces a repetir las letras
    Retorno:
      str: Cadena con el saludo con letras repetidas
    """
    o_varias_veces = "o" * veces
    a_varias_veces = "a" * (veces//2)
    return "h" + o_varias_veces + "l" + a_varias_veces +" "+ nombre
