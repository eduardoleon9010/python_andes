# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:13:37 2024

@author: USUARIO
"""

import calculadora_indices as calc

def calcular_IMC_interactivo():
    """Calcula el Índice de Masa Corporal (IMC) interactivo."""
    print("Calculadora de Índice de Masa Corporal")
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calc.calcular_IMC(peso, altura)
    print(f"Su índice de masa corporal es: {imc:.2f}")

def calcular_porcentaje_grasa_interactivo():
    """Calcula el Porcentaje de Grasa Corporal interactivo."""
    print("Calculadora de Porcentaje de Grasa Corporal")
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M para masculino, F para femenino): ").upper()
    valor_genero = 10.8 if genero == "M" else 0
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"Su porcentaje de grasa corporal es: {porcentaje_grasa:.2f}%")

def calcular_calorias_en_reposo_interactivo():
    """Calcula las calorías en reposo interactivo."""
    print("Calculadora de Calorías en Reposo")
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M para masculino, F para femenino): ").upper()
    valor_genero = 5 if genero == "M" else -161
    calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print(f"Usted quema {calorias_reposo:.2f} calorías en reposo.")

def calcular_calorias_en_actividad_interactivo():
    """Calcula las calorías en actividad interactivo."""
    print("Calculadora de Calorías en Actividad")
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M para masculino, F para femenino): ").upper()
    valor_genero = 5 if genero == "M" else -161
    valor_actividad = float(input("Ingrese el valor de la actividad (según la descripción): "))
    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"Usted quema {calorias_actividad:.2f} calorías realizando la actividad.")

def consumo_calorias_recomendado_para_adelgazar_interactivo():
    """Calcula el consumo calórico recomendado para adelgazar interactivo."""
    print("Calculadora de Consumo Calórico Recomendado para Adelgazar")
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    genero = input("Ingrese su género (M para masculino, F para femenino): ").upper()
    valor_genero = 5 if genero == "M" else -161
    mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(mensaje)

def main():
    """Función principal del programa."""
    print("Bienvenido a la Calculadora de Índices Corporales")
    while True:
        print("\nOpciones:")
        print("1. Calcular Índice de Masa Corporal")
        print("2. Calcular Porcentaje de Grasa Corporal")
        print("3. Calcular Calorías en Reposo")
        print("4. Calcular Calorías en Actividad")
        print("5. Calcular Consumo Calórico Recomendado para Adelgazar")
        print("0. Salir")
        opcion = input("Ingrese el número de la opción que desee (0-5): ")

        if opcion == "1":
            calcular_IMC_interactivo()
        elif opcion == "2":
            calcular_porcentaje_grasa_interactivo()
        elif opcion == "3":
            calcular_calorias_en_reposo_interactivo()
        elif opcion == "4":
            calcular_calorias_en_actividad_interactivo()
        elif opcion == "5":
            consumo_calorias_recomendado_para_adelgazar_interactivo()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 0 al 5.")

if __name__ == "__main__":
    main()
