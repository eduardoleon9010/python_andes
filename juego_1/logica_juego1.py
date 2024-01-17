# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:49:15 2024

@author: USUARIO
"""

import random

def mano_nueva() -> dict:
    """Crea y retorna una nueva mano con dos cartas."""
    mano = {'carta1': carta_nueva(), 'carta2': carta_nueva(), 'tam': 2}
    return mano

def carta_nueva() -> dict:
    """Genera y retorna una nueva carta."""
    palo = nombre_palo(random.randint(1, 4))
    valor = random.randint(1, 13)
    nombre_carta = "{} de {}".format(nombre_valor(valor), palo)
    carta = {"palo": palo, "valor": valor, "nombre": nombre_carta}
    return carta

def agregar_carta(mano: dict) -> dict:
    """Agrega una nueva carta a la mano y retorna la carta agregada."""
    tam_actual = mano['tam']
    nueva_carta = carta_nueva()
    nueva_llave = 'carta{}'.format(tam_actual + 1)
    mano[nueva_llave] = nueva_carta
    mano['tam'] = tam_actual + 1
    return nueva_carta

def nombre_palo(num_palo: int) -> str:
    """Retorna el nombre del palo según el número proporcionado."""
    nombres_palos = ["Picas", "Corazones", "Tréboles", "Diamantes"]
    return nombres_palos[num_palo - 1]

def nombre_valor(valor: int) -> str:
    """Retorna el nombre de la carta según el valor proporcionado."""
    nombres_valores = {1: "AS", 11: "J", 12: "Q", 13: "K"}
    return nombres_valores.get(valor, str(valor))

def contar_puntos_mano(mano: dict) -> int:
    """Calcula y retorna la cantidad de puntos en la mano."""
    puntos = 0
    for i in range(1, 6):
        puntos += contar_puntos_carta(mano, i)
    return puntos

def contar_puntos_carta(mano: dict, numero_carta: int) -> int:
    """Calcula y retorna los puntos de una carta en particular."""
    puntos = 0
    llave = "carta{}".format(numero_carta)
    if llave in mano:
        carta = mano[llave]
        valor = carta["valor"]
        if valor == 1:
            puntos = 11
        elif valor > 10:
            puntos = 10
        else:
            puntos = valor
    return puntos

def casa_debe_continuar(mano_casa: dict) -> bool:
    """Determina si la casa debe continuar agregando cartas."""
    puntos_casa = contar_puntos_mano(mano_casa)
    return puntos_casa < 16 or puntos_casa > 21
