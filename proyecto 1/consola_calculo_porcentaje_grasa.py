# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:27:22 2022

@author: Eduardo
"""
import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa()->None:
    peso=float(input("ingrese peso en kg: "))
    altura=float(input("ingrese altura en m: "))
    edad=int(input("ingrese edad en años: "))
    valor_genero= float(input("ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "))
    GC=calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("El porcentaje de grasa que tiene el cuerpo de la persona es ", GC,"%" )
    
    
def iniciar_aplicacion_GC()->None:
    
    ejecutar_calcular_porcentaje_grasa()
    
ejecutar_calcular_porcentaje_grasa()

