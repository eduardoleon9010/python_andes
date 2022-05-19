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

