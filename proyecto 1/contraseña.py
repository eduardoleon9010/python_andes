# -*- coding: utf-8 -*-
contrasena_almacenada = "secreto"
contrasena_ingresada = input("Ingrese su contraseña:")

if contrasena_almacenada == contrasena_ingresada:
    mensaje = "Su contraseña es correcta"
else:
    mensaje = "La contraseña es incorrecta"

print(mensaje)
