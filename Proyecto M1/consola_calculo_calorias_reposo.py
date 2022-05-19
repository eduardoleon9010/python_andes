# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:34:06 2022

@author: abelator

Con este archivo interactuamos con el usuario para obtener los datos
necesarios para caluclar las calorias necesarias en reposo y devolverselo al usuario
"""

import calculadora_indices as calc
"""
Con la linea anterior importamos el módulo que realiza todos
los cálculos de los diferentes índices
"""

def calorias_reposo() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingresa la altura de la persona (en centimetros): "))
    edad = int(input("Ingresa la edad de la persona (en años): "))
    valor_genero = int(input("Ingresa el valor 5 en caso de ser masculino o -161 en caso de ser femenino: "))
    cal_rep = calc.calcular_calorias_reposo(peso, altura, edad, valor_genero)
    print ("\nLa cantidad de calorias que quema la persona en reposo son: " + str(round(cal_rep, 2)) + " cal")
    
calorias_reposo()