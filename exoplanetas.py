# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:38:25 2023

@author: USUARIO
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Agrega esta línea para importar seaborn
import numpy as np
import cv2


plt.rcParams.update({'font.size': 12})


def cargar_datos(nombre_archivo: str) -> pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv(nombre_archivo)
    return df

def histograma_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por año.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    """
    # Extraer el año de descubrimiento de la columna 'DESCUBRIMIENTO'
    datos['DESCUBRIMIENTO'] = datos['DESCUBRIMIENTO'].apply(lambda x: int(str(x)[:4]))
    
    # Crear el histograma
    plt.hist(datos['DESCUBRIMIENTO'], bins=30, edgecolor='k', alpha=0.7)
    
    # Configurar el gráfico
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Cantidad de Planetas')
    plt.title('Histograma de Descubrimiento de Exoplanetas')
    
    # Mostrar el gráfico
    plt.show()

def estado_publicacion_por_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por año, agrupados de acuerdo con el tipo de publicación.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    """
    # Crear un BoxPlot
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=datos, x='DESCUBRIMIENTO', y='ESTADO_PUBLICACION')
    
    # Configurar el gráfico
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Estado de Publicación')
    plt.title('BoxPlot de Estado de Publicación por Año de Descubrimiento')
    
    # Mostrar el gráfico
    plt.show()

def deteccion_por_descubrimiento(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por año, agrupados de acuerdo con el tipo de detección
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    """
    # Crear un BoxPlot
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=datos, x='DESCUBRIMIENTO', y='TIPO_DETECCION')
    
    # Configurar el gráfico
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Tipo de Detección')
    plt.title('BoxPlot de Tipo de Detección por Año de Descubrimiento')
    
    # Mostrar el gráfico
    plt.show()

def deteccion_y_descubrimiento(datos: pd.DataFrame, anho: int) -> None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un año particular, clasificados de acuerdo
        con el tipo de publicación.
        Si el año es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
        anho (int): el año para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    # Filtrar los datos por año si anho es diferente de 0
    if anho != 0:
        datos = datos[datos['DESCUBRIMIENTO'] == anho]
    
    # Calcular la cantidad de planetas por tipo de publicación
    tipo_deteccion_counts = datos['TIPO_DETECCION'].value_counts()
    
    # Crear un gráfico de pie
    plt.figure(figsize=(8, 8))
    plt.pie(tipo_deteccion_counts, labels=tipo_deteccion_counts.index, autopct='%1.1f%%', startangle=140)
    
    # Configurar el gráfico
    if anho == 0:
        plt.title('Distribución de Tipo de Detección para Todos los Planetas')
    else:
        plt.title(f'Distribución de Tipo de Detección en el Año {anho}')
    
    # Mostrar el gráfico
    plt.show()

def cantidad_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de líneas donde aparece una línea por
        cada tipo de detección y se muestra la cantidad de planetas descubiertos
        en cada año, para ese tipo de detección.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    """
    # Crear un gráfico de líneas
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=datos, x='DESCUBRIMIENTO', y='TIPO_DETECCION', estimator='count', ci=None)
    
    # Configurar el gráfico
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Cantidad de Planetas')
    plt.title('Cantidad de Planetas Descubiertos por Tipo de Detección por Año de Descubrimiento')
    
    # Mostrar el gráfico
    plt.show()

def masa_promedio_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de líneas donde aparece una línea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada año, para ese tipo de detección.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    """
    # Crear un gráfico de líneas
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=datos, x='DESCUBRIMIENTO', y='MASA', hue='TIPO_DETECCION', ci=None)
    
    # Configurar el gráfico
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Masa Promedio de Planetas')
    plt.title('Masa Promedio de Planetas Descubiertos por Tipo')
    # Configurar el gráfico
    plt.xlabel('Año de Descubrimiento')
    plt.ylabel('Masa Promedio de Planetas')
    plt.title('Masa Promedio de Planetas Descubiertos por Tipo de Detección por Año de Descubrimiento')
    plt.legend(title='Tipo de Detección')
    
    # Mostrar el gráfico
    plt.show()

def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame) -> None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama corresponderá
        a un planeta y estará ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    """
    # Crear un gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(datos['MASA'], np.log10(datos['MASA_ESTRELLA']), alpha=0.5)
    
    # Configurar el gráfico
    plt.xlabel('Masa del Planeta')
    plt.ylabel('Logaritmo de la Masa de la Estrella')
    plt.title('Masa de los Planetas vs. Logaritmo de la Masa de las Estrellas')
    
    # Mostrar el gráfico
    plt.show()

def graficar_cielo(datos: pd.DataFrame) -> list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubrirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la información de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representación del cielo
    """
    # Crear una matriz de ceros para representar el cielo
    cielo = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Mapear tipos de detección a colores
    colores = {
        'Radial Velocity': [255, 0, 0],  # Rojo
        'Imaging': [0, 255, 0],         # Verde
        'Eclipse Timing Variations': [0, 0, 255],  # Azul
        # Agregar más mapeos de colores según sea necesario
    }
    
    # Asignar colores a los planetas en la matriz del cielo
    for i, planeta in datos.iterrows():
        x, y = np.random.randint(0, 100), np.random.randint(0, 100)  # Posición aleatoria en la matriz
        color = colores.get(planeta['TIPO_DETECCION'], [128, 128, 128])  # Gris por defecto si no se encuentra el tipo
        cielo[y, x, :] = color
    
    # Mostrar la imagen del cielo
    plt.figure(figsize=(8, 8))
    plt.imshow(cielo)
    plt.axis('off')
    plt.title('Representación del Cielo')
    plt.show()
    
    return cielo

def filtrar_imagen_cielo(imagen: list) -> None:
    """ Le aplica a la imagen un filtro de convolución basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    # Crear un kernel de convolución
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    
    # Aplicar el filtro de convolución
    resultado = cv2.filter2D(imagen, -1, kernel)
    
    # Mostrar la imagen filtrada
    plt.figure(figsize=(8, 8))
    plt.imshow(resultado)
    plt.axis('off')
    plt.title('Imagen del Cielo Filtrada')
    plt.show()

if __name__ == "__main__":
    # Aquí puedes agregar código para probar las funciones si lo deseas
    # Cargar los datos desde un archivo CSV en un DataFrame
     datos = cargar_datos("exoplanetas.csv")

    # Llamar a las funciones con el DataFrame cargado
     histograma_descubrimiento(datos)
     estado_publicacion_por_descubrimiento(datos)
    # ...
     pass
