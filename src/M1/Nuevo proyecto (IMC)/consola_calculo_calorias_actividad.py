import formulas as form
peso=float(input('ingrese el peso de la persona(KG) '))
altura=float(input('ingrese la estatura de la persona(CM) '))
edad=int(input('ingrese la edad de la persona '))
valor_genero=float(input('ingrese el valor 5 en caso de ser hombre si no es asi ingresar el valor -161 '))
valor_actividad=float(input('ingrese el numero respecto a la actividad fisica que usted practica: 1.2: poco o ningún ejercicio, 1.375: ejercicio ligero (1 a 3 días a la semana), 1.55: ejercicio moderado (3 a 5 días a la semana), 1.725: deportista (6 -7 días a la semana), 1.9: atleta (entrenamientos mañana y tarde) '))
reposo=form.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
resultado=reposo*valor_actividad
print(str(resultado )+'CALORIAS')