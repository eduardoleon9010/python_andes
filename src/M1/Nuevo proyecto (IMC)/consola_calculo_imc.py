import formulas as form
peso=float(input('ingrese el peso de la persona(KG) '))
altura=float(input('ingrese la estatura de la persona(M) '))
q=form.calcular_IMC(peso, altura)
p=str(q)
print('el IMC segund los datos que proporxiono es de '+ p)





