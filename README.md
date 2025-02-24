# IAImageRecognition

Este proyecto permite generar imágenes a partir de un archivo `.json` que describe las figuras de la imagen y almacenarlas en una carpeta específica. Además, proporciona un script de prueba para generar archivos JSON con imágenes aleatorias para poder realizar las pruebas necesarias.

## Estructura del Proyecto

El proyecto contiene las siguientes carpetas y archivos:

- **main/**: Contiene el archivo principal `main.py` y el script para crear imágenes `createImage.py`, así como la carpeta `assets` que describe las escenas.
- **imagenes/**: Carpeta donde se almacenan las imágenes generadas.
- **Pruebas/**: Carpeta que contiene un script para generar archivos JSON con imágenes aleatorias y almacenarlas en carpetas correspondientes.

## Uso

### Generación de una Imagen

1. Ejecuta el script principal `main.py` para generar la imagen. El script invoca a `createImage.py` para crear la imagen basándose en el archivo JSON.

   ```bash
   python main/main.py
   ```

   Esto creará la imagen y la almacenará en la carpeta `imagenes/` con un nombre generado automáticamente, dicho nombre inicia con el prefijo "imagen", luego los últimos 5 caracteres de el archivo JSON elegido, y por ultimoi la fecha en la que se genera dicha imagen.

### Pruebas

El proyecto incluye un script de pruebas que genera archivos JSON con imágenes aleatorias para realizar validaciones.

1. Para generar un archivo JSON con imágenes aleatorias, dirígete a la carpeta `Pruebas/` y ejecuta el script de prueba.

   ```bash
   python Pruebas/generateFigures.py
   ```

   Este script creará un archivo JSON en una subcarpeta con el nombre del número de figuras que contiene. Esto para separarlos en caso de realizar pruebas unitarias y específicas.

2. Puedes usar estos archivos JSON generados para probar que el script `createImage.py` está funcionando correctamente al generarse las imágenes de acuerdo con las especificaciones del JSON.

   2.1 Para realizar esto, copia los JSON generados y pegalos en la carpeta `assets`, pues el creador de imagenes lee los archivos almacenados en dicha carpeta y los lista al leerlos.
  
Este `README.md` cubre los puntos clave de cómo usar el programa, cómo generar imágenes, cómo hacer pruebas y los pasos a seguir para continuar el desarrollo.
