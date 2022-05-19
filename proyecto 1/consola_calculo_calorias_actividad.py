# -*- coding: utf-8 -*-
import calculadora_indices as calc
def ejecutar_calcular_calorias_en_actividad()->None:
    peso=float(input("ingrese peso en kg: "))
    altura = float(input("ingrese altura  en cm: "))
    edad=int(input("ingrese edad de la persona en años: "))
    valor_genero=float(input("ingrese 5 masculino y -161 si es femenino: "))
    valor_actividad=mostrar_opciones_valor_actividad()
    
    TMBactividad_fisica=calc.calcular_calorias_en_actividad(peso,altura,
                                                            edad,valor_genero,
                                                            valor_actividad)
    print("la cantidad de calorias quemadas es", TMBactividad_fisica,"cal" )
    
def mostrar_opciones_valor_actividad()->None:
    print("ingrese valor de actividad fisica\n")
    print("1.2: poco o ningun ejercicio")
    print("1.375: ejercicio ligero")
    print("1.55: ejercicio moderado")
    print("1.725: deportista")
    print("1.9: atleta")
    opcion=float(input("ingrese opcion: "))
    return opcion
ejecutar_calcular_calorias_en_actividad()

