# -*- coding: utf-8 -*-
"""
Análisis de Datos de Exoplanetas
Este script realiza análisis exploratorio de datos sobre exoplanetas, incluyendo visualizaciones como histogramas, boxplots, diagramas de dispersión y generación de imágenes del cielo. Utiliza datos de exoplanetas provenientes de un archivo CSV y bibliotecas como pandas, matplotlib, seaborn y OpenCV.
"""



import exoplanetas as mod  # Importa el módulo 'exoplanetas' con funciones de análisis de datos relacionados con exoplanetas
import pandas as pd  # Importa la biblioteca pandas para el manejo de datos
import numpy as np  # Importa la biblioteca NumPy para trabajar con matrices
import cv2  # Importa OpenCV para la manipulación de imágenes
import matplotlib.pyplot as plt



def cargar_datos() -> pd.DataFrame:
    """
    Solicita al usuario el nombre del archivo CSV que desea cargar y utiliza la función
    cargar_datos del módulo exoplanetas para construir un DataFrame.
    
    Returns:
        Un DataFrame con los datos contenidos en el archivo CSV.
    """
    # Solicitar al usuario el nombre del archivo CSV
    nombre_archivo = input("Ingrese el nombre del archivo que desea cargar: ")
    # Cargar los datos utilizando la función cargar_datos del módulo exoplanetas
    datos = mod.cargar_datos(nombre_archivo)
    # Obtener la cantidad de registros y nombres de columnas del DataFrame cargado
    cantidad = len(datos)
    columnas = "\n - ".join(datos.columns)
    # Mostrar información sobre los datos cargados
    print(f"Un archivo con {cantidad} registros fue cargado.")
    print(f"Las columnas del conjunto de datos son: \n - {columnas}")
    return datos

def menu() -> None:
    """
    Muestra las opciones del menú para que el usuario elija qué análisis realizar.
    """
    print("\n\nOPCIONES")
    print("0. Cargar datos")
    print("1. Número de descubrimientos por año (histograma)")
    print("2. Descubrimiento por estado de publicación (boxplot)")
    print("3. Descubrimiento por tipo de detección (boxplot)")
    print("4. Tipo de detección por año (pie)")
    print("5. Cantidad de descubrimientos por año según el tipo de detección (líneas)")
    print("6. Masa promedio por año y por tipo de detección (líneas)")
    print("7. Masa de los planetas vs. masa de la estrella más cercana")
    print("8. Graficar cielo")
    print("9. Afinar la imagen del cielo")
    print("10. Salir")

def iniciar_aplicacion() -> None:
    """
    Inicia la aplicación y permite al usuario elegir entre diferentes opciones del menú para realizar análisis.
    """
    datos = None  # Inicializar los datos como None
    continuar = True
    while continuar:
        menu()
        elegido = int(input("Seleccione una opción del menú: "))
        if elegido == 0:
            datos = cargar_datos()
        elif datos is None:
            print("Primero debe cargar los datos (opción 0)")
        elif elegido == 1:
            mod.histograma_descubrimiento(datos)
        elif elegido == 2:
            mod.estado_publicacion_por_descubrimiento(datos)
        elif elegido == 3:
            mod.deteccion_por_descubrimiento(datos)
        elif elegido == 4:
            # Solicitar al usuario el año para el análisis
            anho = int(input("Ingrese el año que desea analizar. Para todos los años ingrese 0: "))
            mod.deteccion_y_descubrimiento(datos, anho)
        elif elegido == 5:
            mod.cantidad_y_tipo_deteccion(datos)
        elif elegido == 6:
            mod.masa_promedio_y_tipo_deteccion(datos)
        elif elegido == 7:
            mod.masa_planetas_vs_masa_estrellas(datos)
        elif elegido == 8:
            generar_imagen_cielo(datos)
        elif elegido == 9:
            afinar_imagen_cielo()
        elif elegido == 10:
            continuar = False
        else:
            print("Seleccione una opción válida del menú")

def generar_imagen_cielo(datos: pd.DataFrame) -> np.ndarray:
    """
    Genera una imagen del cielo con los planetas representados por píxeles de diferentes colores.
    
    Parameters:
        datos (pd.DataFrame): El DataFrame con los datos de los planetas.
        
    Returns:
        np.ndarray: La matriz de la imagen del cielo.
    """
    # Crear una imagen de 100 filas x 200 columnas con píxeles negros
    cielo = np.zeros((100, 200, 3), dtype=np.uint8)
    
    # Mapear tipos de detección a colores
    colores = {
        'Radial Velocity': [255, 0, 0],  # Rojo
        'Imaging': [0, 255, 0],           # Verde
        'Eclipse Timing Variations': [0, 0, 255],  # Azul
        # Agregar más mapeos de colores según sea necesario
    }
    # Asignar colores a los planetas en la matriz del cielo
    for i, planeta in datos.iterrows():
        # Calcular las coordenadas del píxel correspondiente
        x = int((planeta['RA'] / 360) * cielo.shape[1])
        y = int((planeta['DEC'] / 180) * cielo.shape[0])
        # Obtener el color correspondiente al tipo de detección del planeta
        color = colores.get(planeta['TIPO_DETECCION'], [128, 128, 128])  # Gris por defecto si no se encuentra el tipo
        # Asignar el color al píxel en la posición calculada
        cielo[y, x, :] = color
    
    # Mostrar la imagen del cielo
    plt.figure(figsize=(10, 5))
    plt.imshow(cielo)
    plt.axis('off')
    plt.title('Representación del Cielo')
    plt.show()
    
    return cielo

def afinar_imagen_cielo() -> None:
    """
    Afinar la imagen del cielo aplicando una operación de convolución con una máscara predefinida.
    """
    # Obtener la imagen del cielo
    imagen_cielo = generar_imagen_cielo(datos)
    
    # Definir la máscara de convolución
    mascara = np.array([[-1, -1, -1],
                        [-1, 9, -1],
                        [-1, -1, -1]])
    
    # Aplicar el filtro de convolución
    imagen_afinada = cv2.filter2D(imagen_cielo, -1, mascara)
    
    # Mostrar la imagen afinada
    plt.figure(figsize=(10, 5))
    plt.imshow(imagen_afinada)
    plt.axis('off')
    plt.title('Imagen del Cielo Afinada')
    plt.show()

# Iniciar la aplicación
iniciar_aplicacion()
  
   

