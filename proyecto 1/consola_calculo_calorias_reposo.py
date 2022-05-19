# -*- coding: utf-8 -*-
import calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo()->None:
    peso=float(input("ingrese peso en kg: "))
    altura=float(input("ingrese altura en cm: "))
    edad=int(input(("ingrese edad en años: ")))
    valor_genero=int(input("en caso de ser masculino ingrese 5 y en caso de ser femenino ingrese -161: "))
    TMB=calc.calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    print("La cantidad de calorías que la persona quema en reposo es ",TMB)
    
def ejecutar_aplicacion_TMB()->None:
    ejecutar_calcular_calorias_en_reposo()

ejecutar_calcular_calorias_en_reposo()
