import math

def area_poligono(longitud_lado: float, num_lados: int) -> float:
    """
    Calcula y redondea a dos decimales el área de un polígono regular 
    conociendo la longitud de un lado y el número de lados.
    
    Args:
    longitud_lado (float): Longitud de un lado del polígono.
    num_lados (int): Número de lados del polígono.
    
    Returns:
    float: Área del polígono redondeada a dos decimales.
    """
    perimetro = longitud_lado * num_lados
    apotema = longitud_lado / (2 * math.tan(math.pi / num_lados))
    area = 0.5 * perimetro * apotema
    return round(area, 2)
