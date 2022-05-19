"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    
    pelicula = {"nombre": nombre, "genero": genero, "duracion": duracion, "anio": anio,
                "clasificacion": clasificacion, "hora": hora, "dia": dia}
    
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    pelicula = None
    
    if nombre_pelicula == p1.get("nombre"):
        pelicula = p1
        
    if nombre_pelicula == p2.get("nombre"):
        pelicula = p2
        
    if nombre_pelicula == p3.get("nombre"):
        pelicula = p3
    
    if nombre_pelicula == p4.get("nombre"):
        pelicula = p4
        
    if nombre_pelicula == p5.get("nombre"):
        pelicula = p5
    
    return pelicula

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """ 
    
    pelicula_mas_larga = p1
    
    if pelicula_mas_larga.get('duracion') < p2.get("duracion"):
        pelicula_mas_larga = p2
        
    if pelicula_mas_larga.get('duracion') < p3.get("duracion"):
        pelicula_mas_larga = p3
        
    if pelicula_mas_larga.get('duracion') < p4.get("duracion"):
        pelicula_mas_larga = p4
    
    if pelicula_mas_larga.get('duracion') < p5.get("duracion"):
        pelicula_mas_larga = p5
    
    return pelicula_mas_larga

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    
    promedio = (p1.get("duracion") + p2.get("duracion") + p3.get("duracion") + p4.get("duracion")
                + p5.get("duracion")) // 5
    
    horas = str(promedio // 60)
    minutos = str(promedio % 60)
    
    if len(horas) < 2:
        horas = '0'+str(promedio // 60)
    
    return horas + ":" + minutos

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    
    anio_p1 = p1.get('anio')
    anio_p2 = p2.get('anio')
    anio_p3 = p3.get('anio')
    anio_p4 = p4.get('anio')
    anio_p5 = p5.get('anio')
    
    max_anio_peliculas = max(anio_p1, anio_p2, anio_p3, anio_p4, anio_p5)
    
    
    if max_anio_peliculas > anio:
        
        mensaje = []
        
        if anio_p1 > anio:
            mensaje.append(p1.get('nombre'))
        
        if anio_p2 > anio:            
            mensaje.append(p2.get('nombre'))
        
        if anio_p3 > anio:
            mensaje.append(p3.get('nombre'))
            
        if anio_p4 > anio:
            mensaje.append(p4.get('nombre'))
            
        if anio_p5 > anio:
            mensaje.append(p5.get('nombre'))
        
    else:
        mensaje = ["Ninguna"]
        
    
    return ', '.join(mensaje)

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    
    cuantas = 0
    
    if p1.get("clasificacion") == "18+":
        cuantas += 1
    
    if p2.get("clasificacion") == "18+":
        cuantas += 1
        
    if p3.get("clasificacion") == "18+":
        cuantas += 1
        
    if p4.get("clasificacion") == "18+":
        cuantas += 1
        
    if p5.get("clasificacion") == "18+":
        cuantas += 1
    
    
    return cuantas

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    
    reagendar = True
    pelicula_a_reagendar = encontrar_pelicula(peli.get('nombre'), p1, p2, p3, p4, p5).copy()
    

    pelicula_a_reagendar['dia'] = nuevo_dia
    pelicula_a_reagendar['hora'] = nueva_hora
    
    hora_final_reagendar = nueva_hora + (pelicula_a_reagendar.get('duracion') // 60 ) * 100  + (pelicula_a_reagendar.get('duracion') % 60 )
    dias_de_la_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        
    if nuevo_dia == p1.get('dia'):
        hora_final_agendada = p1.get('hora') + (p1.get('duracion') // 60) * 100 + (p1.get('duracion') % 60)
        if hora_final_reagendar > p1.get('hora') and hora_final_agendada > nueva_hora:
            reagendar = False
            
    if nuevo_dia == p2.get('dia'):
        hora_final_agendada = p2.get('hora') + (p2.get('duracion') // 60) * 100 + (p2.get('duracion') % 60)
        if hora_final_reagendar > p2.get('hora') and hora_final_agendada > nueva_hora:
            reagendar = False
            
    if nuevo_dia == p3.get('dia'):
        hora_final_agendada = p3.get('hora') + (p3.get('duracion') // 60) * 100 + (p3.get('duracion') % 60)
        if hora_final_reagendar > p3.get('hora') and hora_final_agendada > nueva_hora:
            reagendar = False
           
    if nuevo_dia == p4.get('dia'):
        hora_final_agendada = p4.get('hora') + (p4.get('duracion') // 60) * 100 + (p4.get('duracion') % 60)
        if hora_final_reagendar > p4.get('hora') and hora_final_agendada > nueva_hora:
            reagendar = False         
            
    if nuevo_dia == p5.get('dia'):
        hora_final_agendada = p5.get('hora') + (p5.get('duracion') // 60) * 100 + (p5.get('duracion') % 60)
        if hora_final_reagendar > p3.get('hora') and hora_final_agendada > nueva_hora:
            reagendar = False
            
            
    if control_horario == True:
        
        if "Documental" in pelicula_a_reagendar['genero'] and pelicula_a_reagendar.get('hora') >= 2200:
            reagendar = False
            
        if 'Drama' in pelicula_a_reagendar['genero'] and pelicula_a_reagendar.get('dia') == 'Viernes':
            reagendar = False
            
        if pelicula_a_reagendar.get('dia') in dias_de_la_semana and pelicula_a_reagendar.get('hora') < 600:
            reagendar = False
        
        if pelicula_a_reagendar.get('dia') in dias_de_la_semana and pelicula_a_reagendar.get('hora') >= pelicula_a_reagendar.get('hora') >= 2300:
                        reagendar = False
        
    if reagendar:
        
        encontrar_pelicula(peli.get('nombre'), p1, p2, p3, p4, p5)['dia'] = nuevo_dia
        encontrar_pelicula(peli.get('nombre'), p1, p2, p3, p4, p5)['hora'] = nueva_hora    
        
    return reagendar

    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
        
    puede_invitar = True
    
    if edad_invitado < 18:
        
        if peli['clasificacion'] == '18+':
            puede_invitar = False
            
            if 'Documental' in peli['genero']:
                puede_invitar = True
            
        if autorizacion_padres:
            puede_invitar = True
        
        if edad_invitado < 16:
            
            if peli['clasificacion'] == '16+':
                puede_invitar = False
                
                if 'Documental' in peli['genero']:
                    puede_invitar = True
            
            if autorizacion_padres:
                puede_invitar = True
            
            if edad_invitado < 15:
            
                if 'Terror' in peli['genero']:
                    puede_invitar = False
            
                elif edad_invitado < 13:
                    
                    if peli['clasificacion'] == '13+':
                        puede_invitar = False
                        
                        if 'Documental' in peli['genero']:
                            puede_invitar = True
                        
                    if autorizacion_padres:
                        puede_invitar = True
                        
                    
                    if edad_invitado <= 10:
                        
                        if edad_invitado < 7 and peli['clasificacion'] == '7+':
                            puede_invitar = False
                            
                            if autorizacion_padres:
                                puede_invitar = True
                            
                        if 'Familiar' not in peli['genero']:
                            puede_invitar = False
                            
    
    return puede_invitar