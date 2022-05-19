# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:59:58 2021

@author: abelator

Aquí realizaremos los cálculos para obtener los índices 
según los paremetros introducidos por el usuario en otro módulo
que invocará a este
"""

def calcular_IMC(peso:float, altura:float)->float:
    """
    Calcula el índice de masa corporal de una persona a partir de la ecuación.
    
    Parameters
    ----------
    peso : float
        de la persona en kg.
    altura : float
        de la persona en metros.

    Returns
    -------
    float
        Índice de masa corporal.
    """
    IMC = peso/pow(altura, 2)
    return IMC

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->float:
    """
    Calcula el porcentaje de grasa de una persona a partir de la ecuación.
   
    Parameters
    ----------
    peso : float
        en kg.
    altura : float
        en metros.
    edad : int
        en años.
    valor_genero : float
        masculino 10.8 y femenino 0.

    Returns
    -------
    float
        Porcentaje de grasa del cuerpo.
    """
    PGC = 1.2 * peso/pow(altura, 2) + 0.23 * edad - 5.4 - valor_genero
    return PGC

def calcular_calorias_reposo(peso:float, altura:float, edad:int,
                             valor_genero:int)->float:
    """
    Calorias quemadas en reposo = tasa metabólica basal.
    
    Parameters
    ----------
    peso : float
        en kg.
    altura : float
        en centimetros.
    edad : int
        en años.
    valor_genero : int
        masculino 5 y femenino -161.

    Returns
    -------
    float
        tasa metabólica basal.
    """
    TMB = 10*peso + 6.25*altura - 5*edad + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int,
                             valor_genero:int, valor_actividad:float)->float:
    """
    Calorias quemadas en actividad = tmb según actividad.
    
    Parameters
    ----------
    peso : float
        en kg.
    altura : float
        en centimetros.
    edad : int
        en años.
    valor_genero : int
        masculino 5 y femenino -161.
    valor_actividad: float
        según su intensidad semanal 1.2, 1.375, 1.55, 1.72, 1.9

    Returns
    -------
    float
        tasa metabólica basal en actividad.
    """
    TMBA =  (10*peso + 6.25*altura - 5*edad + valor_genero) * valor_actividad
    return TMBA

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int,
                             valor_genero:int)->float:
    """
    Rango calorias diarias recomendadas para adelgazar.
    
    Parameters
    ----------
    peso : float
        en kg.
    altura : float
        en centimetros.
    edad : int
        en años.
    valor_genero : int
        masculino 5 y femenino -161.

    Returns
    -------
    float
        dos valores, mínimo y máximo dentro de una cadena.
    """
    TMB = 10*peso + 6.25*altura - 5*edad + valor_genero
    CCR_minimo = round(TMB * 0.8, 2)
    CCR_maximo = round(TMB * 0.85 , 2)
    return (str(CCR_minimo ) + " y " + str(CCR_maximo))
    #return("Para adelgazar es recomendado que consumas entre: " + str(CCR_minimo) + " y " + str(CCR_maximo))

#print(calcular_IMC(71, 1.78)) #solo para probar buen funcionamiento
#print(calcular_porcentaje_grasa(71, 1.78, 42, 10.8))
#print(calcular_calorias_reposo(71, 1.78, 42, 5))
#print(calcular_calorias_en_actividad(71, 1.78, 42, 5,1.55))
#print(consumo_calorias_recomendado_para_adelgazar(71, 1.78, 42, 5))