# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:49:55 2022

@author: abelator

Con este archivo interactuamos con el usuario para obtener los datos
necesarios para caluclar las calorias necesarias según la actividad física y devolverselo al usuario
"""

import calculadora_indices as calc
"""
Con la linea anterior importamos el módulo que realiza todos
los cálculos de los diferentes índices
"""

def calorias_actividad() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura = float(input("Ingresa la altura de la persona (en centimetros): "))
    edad = int(input("Ingresa la edad de la persona (en años): "))
    valor_genero = int(input("Ingresa el valor 5 en caso de ser masculino o -161 en caso de ser femenino: "))
    valor_actividad = float(input("Ingresa el valor 1.2 (para poco o ningún ejercicio); 1.375 (para ejercicio de 1 a 3 días a la semana); 1.55 (para ejercicio de 5 a 10 días a la semana); 1.72 (para ejercicio 6-7 días a la semana); 1.9 (para entrenamientos mañana y tarde): "))
    cal_act = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print ("\nLa cantidad de calorias que quema la persona, según la actividad física que realiza a la semana son: " + str(round(cal_act, 2)) + " cal")
    
calorias_actividad()