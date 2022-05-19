# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:55:22 2022

@author:Eduardo
"""
'''
módulo en el que vas a hacer varios cálculos sobre los indicadores que
presentamos anteriormente.
'''

def calcular_IMC(peso: float,
                 altura: float)->float:
    #formula
    IMC_persona=peso / altura**2 
    
    return IMC_persona


def calcular_porcentaje_grasa(peso: float, 
                              altura:float,
                              edad:int,
                              valor_genero:int)-> float:
    '''
    Calcula el porcentaje de grasa de una persona a partir de la ecuación    

    '''
    GC = 1.2 * calcular_IMC(peso,altura) + 0.23 * edad - 5.4 - valor_genero   
    #edad en años
    #valor genero: H=10.8 M=0
    return round(GC, 2)






def calcular_calorias_en_reposo(peso:float,
                                altura:float, #cm
                                edad:int,
                                valor_genero:int)->float:
    # valor genero =Valor que varía según el género 
    # masculino debe ser 5, femenino -161
    TMB=(10*peso)+(6.25*altura)-(5*edad)+valor_genero
    return round(TMB, 2)







def calcular_calorias_en_actividad(peso:float,
                                   altura:float,
                                   edad:int,
                                   valor_genero:int,
                                   valor_actividad:float)-> float:
    
    TMBactividad_fisica=calcular_calorias_en_reposo(peso,altura,
                                                    edad,valor_genero)*valor_actividad
    return round(TMBactividad_fisica,2)


def consumo_calorias_recomendado_para_adelgazar(peso: float,
                                                altura:float,
                                                edad: int,
                                                valor_genero: int)->str:
    
    CCDA = (calcular_calorias_en_reposo(peso,
                                      altura,
                                      edad,
                                      valor_genero)*(20/100))
    CCDA_2=(calcular_calorias_en_reposo(peso,altura,
                                        edad,valor_genero)*(15/100))
    CDA = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)-CCDA
    
    CDA_2 = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)-CCDA_2
    
    print("Para adelgazar es recomendado que consumas entre: ",round(CDA, 2)," y " ,round(CDA_2, 2)," calorías al día.")
    # valor_genero = masculino 5 y femenino -161.
    














