# -*- coding: utf-8 -*-
nueva = input("Introduzca su nueva contraseña:")
contrasena_correcta = True
mensaje = ""

if longitud(nueva) < 8:
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos 8 caracteres" + "\n"
    
if nueva == contrasena_anterior:
    contrasena_correcta = False
    mensaje += "La nueva contraseña no puede ser igual a la anterior" + "\n"

if nueva.isalnum():
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener signos de puntuación" + "\n"
    
if not tiene_numeros(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos un número" + "\n"

if not tiene_mayusculas(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos una letra mayúscula" + "\n"

if not tiene_minúsculas(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos una letra minúscula" + "\n"

if contrasena_correcta:
    cambiar_contrasena(nueva)
    mensaje = "La contraseña se cambió exitosamente"

print(mensaje)
