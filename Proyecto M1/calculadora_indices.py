# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:04:15 2023

@author: Ing. Leon
"""

"""Proyecto en Python para calcular índices corporales
 como el índice de masa corporal (IMC) y la tasa 
 metabólica basal (TMB) con una interfaz de usuario 
 basada en consola. Aquí tienes una guía paso a paso 
 para crear este proyecto:"""

# calculadora_indices.py

def calcular_IMC(peso: float, altura: float) -> float:
    '''
    Calcula el índice de masa corporal (IMC) de una persona a partir del peso y la altura.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en metros.
    :return: Índice de masa corporal (IMC) de la persona.
    '''
    IMC = peso / (altura ** 2)
    return IMC

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    '''
    Calcula el porcentaje de grasa de una persona a partir del peso, la altura, la edad y el valor de género.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en metros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género: 10.8 para masculino, 0 para femenino.
    :return: Porcentaje de grasa de la persona.
    '''
    GC = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero
    return GC

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    '''
    Calcula la cantidad de calorías que una persona quema estando en reposo (tasa metabólica basal) a partir del peso, la altura, la edad y el valor de género.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en centímetros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género: 5 para masculino, -161 para femenino.
    :return: Tasa metabólica basal (TMB) de la persona en calorías.
    '''
    TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    '''
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física a partir del peso, la altura, la edad, el valor de género y el valor de actividad.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en centímetros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género: 5 para masculino, -161 para femenino.
    :param valor_actividad: Valor que depende de la actividad física semanal (ejemplo: 1.2 para poco o ningún ejercicio).
    :return: Cantidad de calorías quemadas al realizar la actividad física.
    '''
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    TMB_actividad_fisica = TMB * valor_actividad
    return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    '''
    Calcula el rango de calorías recomendado para adelgazar a partir del peso, la altura, la edad y el valor de género.

    :param peso: Peso de la persona en kilogramos.
    :param altura: Altura de la persona en centímetros.
    :param edad: Edad de la persona en años.
    :param valor_genero: Valor que varía según el género: 5 para masculino, -161 para femenino.
    :return: Rango de calorías recomendado para adelgazar en formato de cadena.
    '''
    CCDA = (calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * (20 / 100))
    CCDA_2 = (calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * (15 / 100))
    CDA = calcular_calorias_en_reposo(peso, altura, edad, valor_genero) - CCDA
    CDA_2 = calcular_calorias_en_reposo(peso, altura, edad, valor_genero) - CCDA_2
    
    resultado = f"Para adelgazar es recomendado que consumas entre: {CDA:.2f} y {CDA_2:.2f} calorías al día."
    return resultado

# Ejemplo de uso:
# Si deseas calcular el rango de calorías recomendado para adelgazar, puedes llamar a esta función de la siguiente manera:
# resultado = consumo_calorias_recomendado_para_adelgazar(70, 175, 30, 5)  # Ejemplo con datos ficticios
# print(resultado)
