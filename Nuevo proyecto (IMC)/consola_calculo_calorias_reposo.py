import formulas as form
peso=float(input('ingrese el peso de la persona(KG) '))
altura=float(input('ingrese la estatura de la persona(CM) '))
edad=int(input('ingrese la edad de la persona '))
valor_genero=float(input('ingrese el valor 5 en caso de ser hombre si no es asi ingresar el valor -161 '))
resultado=(10*peso)+(6.25*altura)-(5*edad)+valor_genero
print(resultado)