# -*- coding: utf-8 -*-
def f(x: int)->bool:
    print('f:', x)
    return True

def g(x: int)->bool:
    print('g:', x)
    return False

print("Caso 1 - f and f and f :")
print(f(1) and f(2) and f(3))

print("Caso 2 - f and f and g :")
print(f(1) and f(2) and g(3))

print("Caso 3 - f and g and g :")
print(f(1) and g(2) and g(3))

print("Caso 4 - g and g and g :")
print(g(1) and g(2) and g(3))

print("Caso 1 - f or f or f :")
print(f(1) or f(2) or f(3))

print("Caso 2 - f or f or g :")
print(f(1) or f(2) or g(3))

print("Caso 3 - g or f or g :")
print(g(1) or f(2) or g(3))

print("Caso 4 - g or g or g :")
print(g(1) or g(2) or g(3))

