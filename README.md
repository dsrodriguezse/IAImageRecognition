# IAImageRecognition

Este proyecto permite generar imágenes a partir de un archivo `scene.json` que describe las figuras de la imagen y almacenarlas en una carpeta específica. Además, proporciona un script de prueba para generar archivos JSON con imágenes aleatorias para poder realizar las pruebas necesarias.

## Estructura del Proyecto

El proyecto contiene las siguientes carpetas y archivos:

- **main/**: Contiene el archivo principal `main.py` y el script para crear imágenes `createImage.py`, así como el archivo `scene.json` que describe las escenas.
- **imagenes/**: Carpeta donde se almacenan las imágenes generadas.
- **Pruebas/**: Carpeta que contiene un script para generar archivos JSON con imágenes aleatorias y almacenarlas en carpetas correspondientes.

## Uso

### Generación de una Imagen

1. Coloca tu archivo `scene.json` en la carpeta `main/`. Este archivo debe describir las figuras que se incluirán en la imagen.

2. Ejecuta el script principal `main.py` para generar la imagen. El script invoca a `createImage.py` para crear la imagen basándose en el archivo JSON.

   ```bash
   python main/main.py
   ```

   Esto creará la imagen y la almacenará en la carpeta `imagenes/` con un nombre generado automáticamente.

### Pruebas

El proyecto incluye un script de pruebas que genera archivos JSON con imágenes aleatorias para realizar validaciones.

1. Para generar un archivo JSON con imágenes aleatorias, dirígete a la carpeta `Pruebas/` y ejecuta el script de prueba.

   ```bash
   python Pruebas/generateFigures.py
   ```

   Este script creará un archivo JSON en una subcarpeta con el nombre del número de figuras que contiene.

2. Puedes usar estos archivos JSON generados para probar que el script `createImage.py` está funcionando correctamente al generarse las imágenes de acuerdo con las especificaciones del JSON.
  
Este `README.md` cubre los puntos clave de cómo usar el programa, cómo generar imágenes, cómo hacer pruebas y los pasos a seguir para continuar el desarrollo.
