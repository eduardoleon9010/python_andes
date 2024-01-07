# Este programa está escrito en el archivo perimetro.py

import math

def perimetro_triangulo(cateto1: float, cateto2: float) -> float:
    """
    Calcula el perímetro de un triángulo rectángulo dada la longitud de sus dos catetos.
    
    Args:
    cateto1 (float): Longitud del primer cateto del triángulo.
    cateto2 (float): Longitud del segundo cateto del triángulo.
    
    Returns:
    float: Longitud del perímetro del triángulo.
    """
    hipotenusa = calcular_hip(cateto1, cateto2)
    return cateto1 + cateto2 + hipotenusa

def calcular_hip(cateto1: float, cateto2: float) -> float:
    """
    Calcula la longitud de la hipotenusa en un triángulo rectángulo dada la longitud de sus dos catetos.
    
    Args:
    cateto1 (float): Longitud del primer cateto del triángulo.
    cateto2 (float): Longitud del segundo cateto del triángulo.
    
    Returns:
    float: Longitud de la hipotenusa.
    """
    suma_cuadrados = (cateto1 ** 2) + (cateto2 ** 2)
    hipotenusa = math.sqrt(suma_cuadrados)  # Utilizando math.sqrt para calcular la raíz cuadrada
    return hipotenusa

def main():
    # Solicitar al usuario la longitud de los dos catetos
    cadena_cat_1 = input("Indique la longitud del primer cateto: ")
    cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
    
    # Convertir los caracteres dados por el usuario en un número decimal
    cat_1 = float(cadena_cat_1)
    cat_2 = float(cadena_cat_2)
    
    # Llamar a la función con los valores recibidos
    perimetro = perimetro_triangulo(cat_1, cat_2)
    
    # Mostrar el resultado al usuario
    print(f"El perímetro de un triángulo rectángulo que tenga catetos de longitud {cat_1} y {cat_2} es {perimetro}")

if __name__ == "__main__":
    main()
