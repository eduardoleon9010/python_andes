# -*- coding: utf-8 -*-
def rango_numero(x: int)->int:
    if x < 0:
        respuesta = -1
    elif x < 1000:
        respuesta = 0
    elif x <= 10000:
        respuesta = 1
    else:
        respuesta = 2
        
    return respuesta
