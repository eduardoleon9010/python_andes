# -*- coding: utf-8 -*-
def calcular_precio_pasaje(temporada_alta: bool, compania: str, edad: int, estudiante: bool)->int:
    precio = 5000000
    variaciones = 0
    seguro = False
    
    if compania == "ALAS":
        if temporada_alta:
            variaciones += 0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -= 0.1
    elif compania == "VOLAR":
            if temporada_alta:
                variaciones += 0.2
            if edad > 60:
                seguro = True
    if edad < 18:
            variaciones-= 0.5
    precio *= (1+variaciones)
        
    if seguro:
            precio += 100000
            
    return round(precio)


#PROGRAMA PRINCIPAL
temp = bool(int(input("¿Es temporada alta? Ingrese 1 para SI o 0 para NO:")))
compania = (input("Ingrese la compañia por la que ciafara:"))
edad = int(input("Ingrese la edad de la persona:"))
est = bool(int(input("¿Es estudiante? Ingrese 1 para SI i 0 para NO:")))

tarifa = calcular_precio_pasaje(temp, compania, edad, est)

print("La tarifa del pasaje es de $"+str(tarifa)+" COP")