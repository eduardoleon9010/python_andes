"""
Nivel 2: Proyecto agenda de peliculas.
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

IMPORTANTE: Considera lo siguiente en todas las funciones de este módulo:
Las películas están representadas por diccionarios con las siguientes claves y valores:            
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
        nombre (str): Nombre de la película agendada.
        genero (str): Géneros de la película separados por comas.
        duracion (int): Duración en minutos de la película.
        anio (int): Año de estreno de la película.
        clasificacion (str): Clasificación de restricción por edad.
        hora (int): Hora a la cual se planea ver la película, debe estar entre 0 y 2359.
        dia (str): Día de la semana en el cual se planea ver la película.
    Retorna:
        dict: Diccionario con los datos de la película.
    """    
    pelicula = {"nombre": nombre, "genero": genero, "duracion": duracion, "anio": anio,
                "clasificacion": clasificacion, "hora": hora, "dia": dia}
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, *peliculas) -> dict:
    """Encuentra en cuál de los diccionarios de películas se encuentra la película 
       cuyo nombre es dado por parámetro.
       Si no se encuentra la película se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la película que se desea encontrar.
        *peliculas (dict): Conjunto variable de diccionarios que contienen la información de las películas.
    Retorna:
        dict: Diccionario de la película cuyo nombre fue dado por parámetro. 
        None si no se encuentra una película con ese nombre.
    """
    for pelicula in peliculas:
        if nombre_pelicula == pelicula.get("nombre"):
            return pelicula
    return None

def encontrar_pelicula_mas_larga(*peliculas) -> dict:
    """Encuentra la película de mayor duración entre las películas recibidas por
       parámetro.
    Parametros:
        *peliculas (dict): Conjunto variable de diccionarios que contienen la información de las películas.
    Retorna:
        dict: El diccionario de la película de mayor duración.
    """ 
    pelicula_mas_larga = max(peliculas, key=lambda p: p.get('duracion', 0), default=None)
    return pelicula_mas_larga

def duracion_promedio_peliculas(*peliculas) -> str:
    """Calcula la duración promedio de las películas que entran por parámetro. 
       Retorna la duración promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        *peliculas (dict): Conjunto variable de diccionarios que contienen la información de las películas.
    Retorna:
        str: La duración promedio de las películas en formato 'HH:MM'
    """
    total_duracion = sum(pelicula.get("duracion", 0) for pelicula in peliculas)
    promedio = total_duracion // len(peliculas) if len(peliculas) > 0 else 0
    
    horas = str(promedio // 60).zfill(2)
    minutos = str(promedio % 60).zfill(2)
    
    return f"{horas}:{minutos}"

def encontrar_estrenos(anio: int, *peliculas) -> str:
    """Busca entre las películas cuáles tienen como año de estreno una fecha estrictamente
       posterior a la recibida por parámetro.
    Parametros:
        anio (int): Año límite para considerar la película como estreno.
        *peliculas (dict): Conjunto variable de diccionarios que contienen la información de las películas.
    Retorna:
        str: Una cadena con el nombre de la película estrenada posteriormente a la fecha recibida. 
        Si hay más de una película, entonces se retornan los nombres de todas las películas 
        encontradas separadas por comas. Si ninguna película coincide, retorna "Ninguna".
    """
    estrenos = [pelicula["nombre"] for pelicula in peliculas if pelicula.get("anio", 0) > anio]
    return ', '.join(estrenos) if estrenos else "Ninguna"

def cuantas_peliculas_18_mas(*peliculas) -> int:
    """Indica cuántas películas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        *peliculas (dict): Conjunto variable de diccionarios que contienen la información de las películas.
    Retorna:
        int: Numero de películas con clasificación '18+'
    """
    return sum(1 for pelicula in peliculas if pelicula.get("clasificacion") == "18+")

def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, *peliculas) -> bool: 
    """Verifica si es posible reagendar la película que entra por parámetro. Para esto verifica
       si la nueva hora y el nuevo día no entran en conflicto con ninguna otra película, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Película a reagendar.
        nueva_hora (int): Nueva hora a la cual se quiere ver la película.
        nuevo_dia (str): Nuevo día en el cual se quiere ver la película.
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las películas.
        *peliculas (dict): Conjunto variable de diccionarios que contienen la información de las películas.
    Retorna:
        bool: True en caso de que se haya podido reagendar la película, False de lo contrario.
    """
    def conflicto_horario(p1, p2):
        hora_final_p1 = p1.get('hora') + (p1.get('duracion') // 60 ) * 100 + (p1.get('duracion') % 60 )
        hora_final_p2 = p2.get('hora') + (p2.get('duracion') // 60 ) * 100 + (p2.get('duracion') % 60 )
        return hora_final_p1 > p2.get('hora') and hora_final_p2 > nueva_hora

    for pelicula in peliculas:
        if peli["nombre"] != pelicula["nombre"]:
            if nuevo_dia == pelicula.get('dia') and conflicto_horario(peli, pelicula):
                return False
            
            if control_horario:
                if "Documental" in peli['genero'] and nueva_hora >= 2200:
                    return False
                
                if 'Drama' in peli['genero'] and nuevo_dia == 'Viernes':
                    return False
                
                if nuevo_dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves'] and nueva_hora < 600:
                    return False
                
                if nuevo_dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves'] and nueva_hora >= 2300:
                    return False
                
    # Si no hay conflictos, reagendamos la película
    peli['dia'] = nuevo_dia
    peli['hora'] = nueva_hora
    return True

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parámetro a ver la 
       película que entra igualmente por parámetro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Película que se desea ver con el invitado.
        edad_invitado (int): Edad del invitado con quien se desea ver la película.
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorización de sus padres 
        para ver la película.
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    def cumple_restricciones(edad, clasificacion, genero):
        if edad < 18 and clasificacion == '18+':
            if 'Documental' in genero:
                return True
            if autorizacion_padres:
                return True
        if edad < 16 and clasificacion == '16+':
            if 'Documental' in genero:
                return True
            if autorizacion_padres:
                return True
        if edad < 15 and clasificacion == '15+':
            return True
        if edad < 13 and clasificacion == '13+':
            if 'Documental' in genero:
                return True
            if autorizacion_padres:
                return True
        if edad <= 10 and clasificacion == '7+':
            if edad < 7 and autorizacion_padres:
                return True
            if 'Familiar' not in genero:
                return False
        return True

    return cumple_restricciones(edad_invitado, peli['clasificacion'], peli['genero'])
