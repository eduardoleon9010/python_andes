# -*- coding: utf-8 -*-
def calcular_iva_propina_total_factura (costo_factura: int) -> str:
    """ IVA y propina
    Parámetros:
      costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina
    Retorno:
      str: Cadena con el iva, propina y total de la factura, separados por coma
    """
    IVA = round (costo_factura*19/100)
    propina = round (costo_factura*10/100) 
    total = round (costo_factura + propina + IVA)
    return str(IVA) + "," + str(propina) + "," + str(total)
