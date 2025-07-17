import formulas as form
peso=float(input('ingrese el peso de la persona(KG) '))
altura=float(input('ingrese la estatura de la persona(M) '))
edad=int(input('ingrese la edad de la persona '))
valor_genero=float(input('ingrese el valor 10.8 en caso de ser hombre si no es asi ingresar el valor 0 '))
p=1.2*form.calcular_IMC(peso, altura)+0.23*edad-5.24-valor_genero
print(p)
