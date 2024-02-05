"""
Nivel 2: Proyecto agenda de peliculas.
Módulo de interaccion por teclado.


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

"""

import modulos_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """   
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(*peliculas: dict) -> None:
    """
    Ejecuta la opción de encontrar la película más larga.

    Parameters:
    *peliculas (dict): Argumentos variables que contienen información sobre las películas.

    Returns:
    None: Esta función imprime la información de la película más larga en la consola.
    """
    # Llama a la función del módulo correspondiente para encontrar la película más larga
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(*peliculas)

    # Imprime la información de la película más larga
    print(f"La película más larga es {pelicula_mas_larga['nombre']} con una duración de {pelicula_mas_larga['duracion']} minutos")

def ejecutar_consultar_duracion_promedio_peliculas(*peliculas: dict) -> None:
    """Ejecuta la opción de consultar la duración promedio de las películas.

    Parameters:
    *peliculas (dict): Argumentos variables que representan diccionarios de películas.

    Returns:
    None. Imprime la duración promedio de las películas en la consola.
    """
    duracion_promedio = mod.duracion_promedio_peliculas(*peliculas)
    print(f"Duración promedio de películas: {duracion_promedio}")


def ejecutar_encontrar_estrenos(*peliculas: dict) -> None:
    """Ejecuta la opción de buscar películas de estreno.

    Parameters:
    *peliculas (dict): Argumentos variables que representan diccionarios de películas.

    Returns:
    None. Imprime las películas de estreno encontradas en la consola.
    """
    anio_referencia = int(input("¿Cuál año desea que sea la referencia?: "))
    estrenos = mod.encontrar_estrenos(anio_referencia, *peliculas)
    print(f"Películas de estreno encontradas: {estrenos}")


def ejecutar_cuantas_peliculas_18_mas(*peliculas: dict) -> None:
    """Ejecuta la opción de consultar cuántas películas tienen clasificación '18+'.

    Parameters:
    *peliculas (dict): Argumentos variables que representan diccionarios de películas.

    Returns:
    None. Imprime la cantidad de películas con clasificación '18+' en la consola.
    """
    cantidad_18_mas = mod.cuantas_peliculas_18_mas(*peliculas)
    print(f"Existen {cantidad_18_mas} películas con clasificación '18+'.")


def ejecutar_reagendar_pelicula(*peliculas: dict) -> None:
    """Ejecuta la opción de reagendar una película.

    Parameters:
    *peliculas (dict): Argumentos variables que representan diccionarios de películas.

    Returns:
    None. Imprime el resultado del intento de reagendar la película en la consola.
    """
    print("Reagendar una película de la agenda")

    nombre_pelicula = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula_a_reagendar = mod.encontrar_pelicula(nombre_pelicula, *peliculas)
    
    if pelicula_a_reagendar is None:
        print("No hay ninguna película con este nombre")
    else:
        nuevo_dia = input("Digite el día: ")
        nueva_hora = int(input("Digite la nueva hora en formato militar: "))
        control_horario = input("¿Desea control de horario 'N' o 'S'?: ")
        
        if mod.reagendar_pelicula(pelicula_a_reagendar, nueva_hora, nuevo_dia, control_horario, *peliculas):
            print("La película fue reagendada con éxito.")
        else:
            print("No se puede reagendar la película debido a conflictos.")


def ejecutar_decidir_invitar(*peliculas: dict) -> None:
    """Ejecuta la opción de decidir si se puede invitar a alguien a ver una película o no.

    Parameters:
    *peliculas (dict): Argumentos variables que representan diccionarios de películas.

    Returns:
    None. Imprime el resultado de la decisión sobre si se puede invitar a alguien a ver la película en la consola.
    """
    print("Decidir si se puede invitar a alguien a ver una película")

    nombre_pelicula = input("Ingrese el nombre de la película: ")
    pelicula_a_invitar = mod.encontrar_pelicula(nombre_pelicula, *peliculas)
    
    if pelicula_a_invitar is None:
        print("No hay ninguna película con este nombre")
    else:
        edad_invitado = int(input("Ingrese la edad de la persona que desea invitar: "))
        autorizacion_padres = input("¿Tiene autorización de los padres? (Sí/No): ").lower() == "si"
        
        if mod.decidir_invitar(pelicula_a_invitar, edad_invitado, autorizacion_padres):
            print("Puede invitar a la persona a ver la película.")
        else:
            print("No puede invitar a la persona a ver la película debido a restricciones.")


def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.

    La función crea cinco instancias de películas y ejecuta un bucle que muestra información detallada
    sobre cada película y luego presenta un menú de aplicación para que el usuario realice operaciones en ellas.

    Parameters:
    None.

    Returns:
    None.
    """
    pelicula1 = mod.crear_pelicula("Shrek", "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out", "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus", "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception", "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de películas para la semana de receso" + "\n" + ("-" * 50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-" * 50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-" * 50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-" * 50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-" * 50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-" * 50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Muestra al usuario las opciones de ejecución disponibles y ejecuta la opción elegida.

    Parameters:
    p1 (dict): Diccionario de la película 1.
    p2 (dict): Diccionario de la película 2.
    p3 (dict): Diccionario de la película 3.
    p4 (dict): Diccionario de la película 4.
    p5 (dict): Diccionario de la película 5.

    Returns:
    bool: Indica si la aplicación debe continuar ejecutándose (True) o si debe salir (False).
    """
    print("Menu de opciones")
    print(" 1 - Consultar película más larga")
    print(" 2 - Consultar duración promedio de las películas")
    print(" 3 - Consultar películas de estreno")
    print(" 4 - Consultar cuántas películas tienen clasificación 18+")
    print(" 5 - Reagendar película")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

if __name__ == "__main__":
    iniciar_aplicacion()
