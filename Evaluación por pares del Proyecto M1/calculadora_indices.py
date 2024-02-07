# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:13:19 2024

@author: USUARIO
"""

def calcular_IMC(peso: float, altura: float) -> float:
    """
    Calcula el índice de masa corporal de una persona.

    Parameters:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.

    Returns:
    float: Índice de masa corporal de la persona.
    """
    imc = peso / (altura ** 2)
    return imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    """
    Calcula el porcentaje de grasa corporal de una persona.

    Parameters:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.
    edad (int): Edad de la persona en años.
    valor_genero (float): Valor que varía según el género de la persona:
                          10.8 si es masculino, 0 si es femenino.

    Returns:
    float: Porcentaje de grasa corporal de la persona.
    """
    porcentaje_grasa = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero
    return porcentaje_grasa


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    """
    Calcula la cantidad de calorías que una persona quema en reposo (Tasa Metabólica Basal).

    Parameters:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.
    edad (int): Edad de la persona en años.
    valor_genero (int): Valor que varía según el género de la persona:
                        5 si es masculino, -161 si es femenino.

    Returns:
    float: La cantidad de calorías que la persona quema en reposo.
    """
    tmb = 10 * peso + 6.25 * altura * 100 - 5 * edad + valor_genero
    return tmb


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar alguna actividad física.

    Parameters:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.
    edad (int): Edad de la persona en años.
    valor_genero (int): Valor que varía según el género de la persona:
                        5 si es masculino, -161 si es femenino.
    valor_actividad (float): Valor que depende de la actividad física semanal.

    Returns:
    float: La cantidad de calorías que la persona quema realizando la actividad física.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_actividad = tmb * valor_actividad
    return calorias_actividad


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    """
    Calcula el rango de calorías recomendado para adelgazar.

    Parameters:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.
    edad (int): Edad de la persona en años.
    valor_genero (int): Valor que varía según el género de la persona:
                        5 si es masculino, -161 si es femenino.

    Returns:
    str: Una cadena indicando el rango de calorías recomendado para adelgazar.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.8
    rango_superior = tmb * 0.85
    mensaje = f"Para adelgazar es recomendado que consumas entre: {rango_inferior:.2f} y {rango_superior:.2f} calorías al día."
    return mensaje
