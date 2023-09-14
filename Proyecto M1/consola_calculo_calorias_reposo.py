# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:10:30 2023

@author: Ing. Leon
"""

import calculadora_indices as calc

print("Calculadora de Calorías en Reposo (Tasa Metabólica Basal - TMB)")
genero = input("Ingrese su género (H para hombre, M para mujer): ").upper()
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en centímetros: "))
edad = int(input("Ingrese su edad en años: "))

if genero == 'H':
    valor_genero = 5
elif genero == 'M':
    valor_genero = -161
else:
    print("Género no válido")
    exit()

tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"Su TMB es: {tmb:.2f} calorías por día")
