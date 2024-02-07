"""
Created on Sun Sep 10 07:16:47 2023

"""

# Proyecto Billboard: Gestión de Canciones y Estadísticas

Este proyecto es una aplicación de consola que permite gestionar y calcular estadísticas sobre un listado de canciones basado en la famosa tabla Billboard.

## Contenido

- [Descripción](#descripción)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Estructura de Archivos](#estructura-de-archivos)
- [Funciones en 'billboard.py'](#funciones-en-billboardpy)
- [Interfaz de Consola en 'consola_billboard.py'](#interfaz-de-consola-en-consolabillboardpy)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

El objetivo de este proyecto es crear una aplicación para manejar y almacenar un listado de canciones y calcular algunas estadísticas sobre estas. La aplicación permite al usuario realizar las siguientes acciones:

1. Cargar un archivo con las canciones del listado de Billboard.
2. Buscar una canción por nombre y año del ranking y mostrar su información.
3. Consultar las canciones de un año dado.
4. Consultar las canciones de un artista en un período de tiempo definido.
5. Consultar todas las canciones de un artista.
6. Consultar todos los artistas que han interpretado una canción dada.
7. Consultar los artistas más populares.
8. Consultar el artista con más canciones de todos los tiempos.
9. Consultar la lista completa de artistas del Billboard junto con sus canciones.
10. Consultar la cantidad promedio de canciones por artista.

## Requisitos del Sistema

- Python 3.6 o superior.
- Biblioteca estándar de Python.

## Instrucciones de Uso

1. Descarga el proyecto o clónalo desde este repositorio de GitHub.
2. Asegúrate de tener Python 3.6 o superior instalado en tu sistema.
3. Abre una terminal o línea de comandos.
4. Navega hasta la carpeta del proyecto.
5. Ejecuta `python consola_billboard.py` para iniciar la interfaz de consola.
6. Sigue las instrucciones en pantalla para interactuar con la aplicación.

## Estructura de Archivos

La estructura de archivos del proyecto es la siguiente:

- `billboard.py`: Módulo que contiene las funciones relacionadas con la gestión de canciones y estadísticas.
- `consola_billboard.py`: Módulo que implementa la interfaz de consola para el usuario.
- `billboard.csv`: Archivo de ejemplo con datos de canciones en formato CSV.
- Otros archivos y directorios necesarios para el funcionamiento del proyecto.

## Funciones en 'billboard.py'

El módulo `billboard.py` contiene las siguientes funciones:

1. `cargar_canciones(archivo)`: Carga un archivo CSV con información de canciones y retorna una lista de diccionarios.
2. `buscar_cancion(canciones, nombre_cancion, anio)`: Busca una canción por nombre y año y retorna su información.
3. `canciones_anio(canciones, anio)`: Consulta las canciones de un año dado y retorna su información.
4. `canciones_artista_periodo(canciones, nombre_artista, anio_inic, anio_fin)`: Consulta las canciones de un artista en un período de tiempo y retorna su información.
5. `todas_canciones_artista(canciones, nombre_artista)`: Consulta todas las canciones de un artista y retorna su información.
6. `todos_artistas_cancion(canciones, nombre_cancion)`: Consulta todos los artistas que han interpretado una canción y retorna sus nombres.
7. `artistas_mas_populares(canciones, valor_minimo)`: Consulta los artistas más populares y retorna sus nombres y cantidad de canciones.
8. `artista_estrella(canciones)`: Consulta el artista con más canciones de todos los tiempos y retorna su nombre y cantidad de canciones.
9. `artistas_y_sus_canciones(canciones)`: Consulta la lista completa de artistas junto con sus canciones.
10. `promedio_canciones_por_artista(canciones)`: Consulta la cantidad promedio de canciones por artista.

## Interfaz de Consola en 'consola_billboard.py'

El módulo `consola_billboard.py` implementa la interfaz de consola para el usuario. Proporciona un menú interactivo que permite al usuario seleccionar las acciones que desea realizar.

## Ejecución del Proyecto

Para ejecutar el proyecto, sigue las [instrucciones de uso](#instrucciones-de-uso) mencionadas anteriormente.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio en GitHub.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus modificaciones y mejoras.
Asegúrate de que tu código cumple con las pautas de estilo y las convenciones del proyecto.
Realiza pruebas para asegurarte de que tu código funciona correctamente.
Haz commit de tus cambios (git commit -m 'Añadida nueva funcionalidad').
Realiza un push de tu rama (git push origin feature/nueva-funcionalidad).
Abre una solicitud de extracción (pull request) en GitHub.
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

