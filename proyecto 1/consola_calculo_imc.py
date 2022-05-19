# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:23:23 2022

@author:Eduardo
"""
import calculadora_indices as calc

def ejecutar_calcular_IMC()->None:
    peso = float(input("ingrese peso en kg: "))
    altura = float(input("ingrese altura em m: "))
    IMC=calc.calcular_IMC(peso, altura)
    print("Índice de masa corporal de la persona", round(IMC, 2))

def iniciar_aplicacion_IMC()->None:
    ejecutar_calcular_IMC()
    
iniciar_aplicacion_IMC()

