# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 07:48:00 2022

@author: juanc
"""

def cargar_canciones(doc:str)->list:
    
    
    archivo = open(doc)
    titulos = archivo.readline()
    
    canciones = []
    
    linea = archivo.readline()
    
    while len(linea) > 0:
        
        cancion = {}
        
        info_cancion = linea.split(",")
        cancion["posicion"] = info_cancion[0]
        cancion["nombre_cancion"] = info_cancion[1]
        cancion["nombre_artista"] = info_cancion[2]
        cancion["anio"] = info_cancion[3]
        cancion["letra"] = info_cancion[4].strip("\n")
        
        canciones.append(cancion)
        
        linea = archivo.readline()
        
    archivo.close()
    
    return canciones

def buscar_cancion(canciones:list, nombre_can:str, anio_rank:str)->dict:
    cancion_buscada = None
    
    encontrada = False
    i = 0
    
    while encontrada == False and i < len(canciones):
        cancion = canciones[i]
        nom_can = cancion["nombre_cancion"]
        anio_can = cancion["anio"]
        
        if nombre_can == nom_can and anio_rank == anio_can:
            cancion_buscada = cancion
            encontrada = True
        else: 
            i += 1
            
    return cancion_buscada
            
    
lis_canciones = cargar_canciones("billboard.csv")    

def canciones_anio(canciones:list, anio:str)->list:
    cancion_buscada = []
    
    for i in canciones:
        
        anio_can = i["anio"]
        
        if anio_can == anio:
            del i["letra"]
            cancion_buscada.append(i)
            
    return cancion_buscada

def canciones_artista_periodo(canciones:list, nom_artista:str, anio_ini:str, anio_fin: str)->list:
    cancion_buscada = []
    
    for i in canciones:
        
        anio_can = i["anio"]
        artista = i['nombre_artista']
        
        if artista == nom_artista and anio_can >= anio_ini and anio_can <= anio_fin:
            del i["letra"]
            cancion_buscada.append(i)
            
    return cancion_buscada

def todas_canciones_artista(canciones:list, artista:str)->list:
    cancion_buscada = []
    
    for i in canciones:
        
        art = i['nombre_artista']
        
        if artista == art:
            
            del i["letra"]
            
            nom = i["nombre_cancion"]
            
            cancion_buscada.append(nom)
            
    return cancion_buscada
            
def todos_artistas_cancion(canciones:list, can:str)->list:
    cancion_buscada = []
    
    for i in canciones:
        
        nom_can = i["nombre_cancion"]
        
        if nom_can == can:
            del i["letra"]
            
            nom = i['nombre_artista']
            cancion_buscada.append(nom)
            
    return cancion_buscada

def cant_can(canciones:list, artista:str)->list:
    cancion_buscada = []
    
    for i in canciones:
        
        art = i['nombre_artista']
        
        if artista == art:
            
            cancion_buscada.append(i)
            
    return cancion_buscada 
   
def artistas_mas_populares(canciones_lis:list, valor:int)->dict:
    mas_popular = {}

    
    for i in canciones_lis:
        art = i['nombre_artista']
        can = cant_can(canciones_lis, art)
        
        if len(can) > valor:
            
            esta = mas_popular.get(art,None)
        
            if esta == None:
                mas_popular[art] = len(can)
            
    return mas_popular

def artista_estrella(canciones:list)->dict:
    pop = {}
    cant = artistas_mas_populares(canciones, 0)
    
    mayor_can = 0
    mayor_nom = None
    
    for i in cant:
        if cant[i] > mayor_can:
            mayor_can = cant[i]
            mayor_nom = i
            
    pop[mayor_nom] = mayor_can
    
    return pop
    
def artistas_y_sus_canciones(canciones:list)->dict:
    can_art = {}
    
    for i in canciones:
        nombre_art = i['nombre_artista']
        canciones_art = cant_can(canciones, nombre_art)
        
        nom_canciones_art = []
        
        for j in canciones_art:
            nombre_can = j['nombre_cancion']
              
            if not(nombre_can in nom_canciones_art):
                
                nom_canciones_art.append(nombre_can)
            
        can_art[nombre_art] = nom_canciones_art
        
        
    return can_art


def promedio_canciones_por_artista(canciones:list)->float:
    cant_art = 0
    can_can = 0
    
    art_y_can = artistas_y_sus_canciones(canciones)
    
    for i in art_y_can:
        cant_art += 1
        num_can = len(art_y_can[i])
        can_can += num_can
        
    promedio = can_can / cant_art

    
    return promedio
        
            

                    
           
                
            
            

    
    
            
