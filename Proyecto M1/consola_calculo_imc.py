# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:46:38 2022

@author: abelator

Con este archivo interactuamos con el usuario para obtener los datos
necesarios para caluclar el IMC y devolverselo al usuario
"""

import calculadora_indices as calc
"""
Con la linea anterior importamos el módulo que realiza todos
los cálculos de los diferentes índices
"""

def imc() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingresa la altura de la persona (en metros): "))
    #edad = input("Ingrese la edad de la persona (en años): ")
    IMC = calc.calcular_IMC(peso, altura)
    print ("\nEl índice de masa corporal de la persona es: " + str(round(IMC, 2)))
    
imc()