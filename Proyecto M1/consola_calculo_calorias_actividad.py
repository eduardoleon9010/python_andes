# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:10:30 2023

@author: Ing. Leon
"""
import calculadora_indices as calc

print("Calculadora de Calorías con Actividad Física")
sexo = input("Ingrese su sexo (H para hombre, M para mujer): ").upper()
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en centímetros: "))
edad = int(input("Ingrese su edad en años: "))

if sexo == 'H':
    valor_genero = 5
elif sexo == 'M':
    valor_genero = -161
else:
    print("Sexo no válido")
    exit()

actividad = float(input("Ingrese su nivel de actividad:\n1.1: poco o ningún ejercicio\n1.2: ejercicio ligero (1 a 3 días a la semana)\n1.3: ejercicio moderado (3 a 5 días a la semana)\n1.4: deportista (6 -7 días a la semana)\n1.5: atleta (entrenamientos mañana y tarde)\n"))

calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, actividad)
print(f"Su consumo de calorías diario recomendado es: {calorias_actividad:.2f} calorías por día")
