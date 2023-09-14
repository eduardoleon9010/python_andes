# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:10:01 2023

@author: Ing. Leon
"""

import calculadora_indices as calc

print("Calculadora de Índice de Masa Corporal (IMC)")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calc.calcular_IMC(peso, altura)
print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

