# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:10:12 2022

@author: abelator

Con este archivo interactuamos con el usuario para obtener los datos
necesarios para caluclar las calorias necesarias según la actividad física y devolverselo al usuario
"""

import calculadora_indices as calc
"""
Con la linea anterior importamos el módulo que realiza todos
los cálculos de los diferentes índices
"""

def calorias_para_adelgazar() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingresa la altura de la persona (en centimetros): "))
    edad = int(input("Ingresa la edad de la persona (en años): "))
    valor_genero = int(input("Ingresa el valor 5 en caso de ser masculino o -161 en caso de ser femenino: "))
    cal_x_adelg = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print ("\nPara adelgazar es recomendado que consumas entre:  " + (cal_x_adelg) + " calorías al día")
    
calorias_para_adelgazar()

