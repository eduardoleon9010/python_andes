# -*- coding: utf-8 -*-
def es_positivo_de_un_solo_digito_v1 (x: int)->bool:
    if x > 0:
        if x < 10:
            respuesta = True
        else:
            respuesta = False
    else:
        respuesta = False
    return respuesta
        
def es_positivo_de_un_solo_digito_v2(x: int)->bool:
    respuesta = False
    if x > 0 and x < 10:
        respuesta = True
    return respuesta
        
def es_positivo_de_un_solo_digito_v3 (x: int)->bool:
    return x > 0 and x < 10       
        
        