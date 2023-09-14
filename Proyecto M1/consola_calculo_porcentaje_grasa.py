# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:10:18 2023

@author: Ing. Leon
"""

import calculadora_indices as calc

print("Calculadora de Calorías para Adelgazar")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en centímetros: "))
edad = int(input("Ingrese su edad en años: "))
genero = input("Ingrese su género (H para hombre, M para mujer): ").upper()

if genero == 'H':
    valor_genero = 5
elif genero == 'M':
    valor_genero = -161
else:
    print("Género no válido")
    exit()

rango_calorias = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(rango_calorias)
