# -*- coding: utf-8 -*-
import calculadora_indices as calc

def ejecutar_consumo_calorias_para_adelgazar()->None:
    peso = float(input("ingrese el peso en kg: "))
    altura =float(input("ingrese altura en cm: "))
    edad = float(input("ingrese edad en años: "))
    valor_genero=float(input("ingrese 5 masculino y -161 femenino: "))
    CCRA= calc.consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,valor_genero)
    print(CCRA)
   
  
ejecutar_consumo_calorias_para_adelgazar()
    

    
    
    
    
    