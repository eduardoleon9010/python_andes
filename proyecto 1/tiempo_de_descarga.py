# -*- coding: utf-8 -*-

def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int)->int:
    """ Tiempo de descarga
    Parámetros:
      velocidad (int): Velocidad de descarga de la red, en Mbps
      tamanio_archivo (int): Tamaño del archivo a descargar, en GB
    Retorno:
      int: Tiempo estimado en minutos que toma la descarga del archivo
    """
    gb_megas = tamanio_archivo * 1000
    v = velocidad * 8
    tiempo = gb_megas / v
    return round(tiempo)
