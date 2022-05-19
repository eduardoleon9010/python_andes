# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:17:28 2022

@author: abelator

Con este archivo interactuamos con el usuario para obtener los datos
necesarios para caluclar el porcentaje de grasa corporal y devolverselo al usuario
"""

import calculadora_indices as calc
"""
Con la linea anterior importamos el módulo que realiza todos
los cálculos de los diferentes índices
"""

def porcentage_grasa() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingresa la altura de la persona (en metros): "))
    edad = int(input("Ingresa la edad de la persona (en años): "))
    valor_genero = float(input("Ingresa el valor 10.8 en caso de ser masculino o 0 en caso de ser femenino: "))
    porcen_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print ("\nEl porcentaje de grasa de la persona es: " + str(round(porcen_grasa, 2)) + "%")
    
porcentage_grasa()