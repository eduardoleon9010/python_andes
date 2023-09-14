# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:08:12 2023

@author: Ing. Leon
"""

def calcular_IMC(peso, altura):
    """
    Calcula el índice de masa corporal (IMC) de una persona.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en metros.
    :return: Índice de masa corporal (IMC) de la persona.
    """
    return peso / (altura ** 2)

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    """
    Calcula el porcentaje de grasa corporal de una persona.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en metros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género (10.8 para masculino, 0 para femenino).
    :return: El porcentaje de grasa corporal de la persona.
    """
    imc = calcular_IMC(peso, altura)
    porcentaje_grasa = 1.2 * imc + 0.23 * edad - valor_genero
    return porcentaje_grasa

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo (Tasa Metabólica Basal).

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en centímetros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género (5 para masculino, -161 para femenino).
    :return: La cantidad de calorías que la persona quema en reposo.
    """
    altura_metros = altura / 100  # Convertir altura a metros
    tmb = (10 * peso) + (6.25 * altura_metros * 100) - (5 * edad) + valor_genero
    return tmb

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    """
    Calcula la cantidad de calorías que una persona quema al realizar actividad física.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en centímetros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género (5 para masculino, -161 para femenino).
    :param valor_actividad: Valor que depende de la actividad física semanal.
    :return: La cantidad de calorías que la persona quema al realizar actividad física.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_actividad = tmb * valor_actividad
    return calorias_actividad

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    """
    Calcula el rango de calorías recomendado para adelgazar.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en centímetros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género (5 para masculino, -161 para femenino).
    :return: Una cadena indicando el rango de calorías recomendado para adelgazar.
    """
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.8  # Reducción del 20% para adelgazar
    rango_superior = tmb * 0.9  # Reducción del 10% para adelgazar

    mensaje = f"Para adelgazar es recomendado que consumas entre: {int(rango_inferior)} y {int(rango_superior)} calorías al día."
    return mensaje
