from PIL import Image, ImageDraw
import json
import os
from utils import get_color, generar_nombre_archivo, get_carpeta

def cargar_escena(ruta_archivo):
    """
    Carga un archivo JSON y devuelve los datos de la escena.
    """
    with open(ruta_archivo, 'r') as f:
        scene = json.load(f)
    return scene['scene']

def dibujar_escena(scene_data):
    """
    Dibuja una escena a partir de los datos del JSON.
    """
    # Crear una imagen con el tamaño y color de fondo especificados
    width = scene_data['size']['width']
    height = scene_data['size']['height']
    background_color = get_color(scene_data['background'])
    imagen = Image.new('RGB', (width, height), background_color)
    dibujo = ImageDraw.Draw(imagen)

    # Dibujar cada objeto en la escena
    for obj in scene_data['objects']:
        color = get_color(obj['color'])
        points = obj['points']
        
        if obj['type'] == 'circle':
            center = (points['center']['x'], points['center']['y'])
            radius = points['radius']
            dibujo.ellipse(
                [center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius],
                fill=color
            )
        elif obj['type'] == 'rectangle':
            topleft = (points['topleft']['x'], points['topleft']['y'])
            sides = points['sides']
            dibujo.rectangle(
                [topleft[0], topleft[1], topleft[0] + sides['width'], topleft[1] + sides['height']],
                fill=color
            )
        elif obj['type'] == 'triangle':
            vertices = [(p['x'], p['y']) for p in points]
            dibujo.polygon(vertices, fill=color)
        elif obj['type'] == 'ellipse':
            center = (points['center']['x'], points['center']['y'])
            radii = points['radii']
            dibujo.ellipse(
                [center[0] - radii['width'], center[1] - radii['height'], center[0] + radii['width'], center[1] + radii['height']],
                fill=color
            )
        elif obj['type'] == 'square':
            topleft = (points['topleft']['x'], points['topleft']['y'])
            side = points['side']
            dibujo.rectangle(
                [topleft[0], topleft[1], topleft[0] + side, topleft[1] + side],
                fill=color
            )
        elif obj['type'] == 'polygon':
            vertices = [(p['x'], p['y']) for p in points]
            dibujo.polygon(vertices, fill=color)

    return imagen

def guardar_imagen(imagen, nombre_base, sufijo):
    """
    Guarda la imagen generada en la carpeta 'imagenes'.
    """
    nombre_archivo = generar_nombre_archivo(nombre_base, sufijo, "png")
    ruta = get_carpeta('imagenes', nombre_archivo)

    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    # Guardar la imagen generada
    imagen.save(ruta)
    print(f"Guardado en la carpeta imagenes como: {nombre_archivo}")

def procesar_archivo(ruta_archivo):
    """
    Procesa un archivo JSON: carga la escena, la dibuja y guarda la imagen.
    """
    try:
        # Cargar la escena desde el archivo JSON
        scene_data = cargar_escena(ruta_archivo)

        # Dibujar la escena
        imagen = dibujar_escena(scene_data)

        # Guardar la imagen
        nombre_base = "imagen"
        sufijo = os.path.splitext(os.path.basename(ruta_archivo))[0][-5:]
        guardar_imagen(imagen, nombre_base, sufijo)
    except Exception as e:
        print(f"Error al procesar el archivo {ruta_archivo}: {e}")

def main():
    # Listar archivos en la carpeta "assets"
    assets_folder = 'assets'
    files = [f for f in os.listdir(assets_folder) if f.endswith('.json')]

    if not files:
        print("No se encontraron archivos JSON en la carpeta 'assets'.")
        return

    # Mostrar archivos y pedir al usuario que seleccione una opción
    print("Seleccione una opción:")
    print("1. Dibujar una imagen específica")
    print("2. Dibujar todas las imágenes")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        # Opción 1: Dibujar una imagen específica
        print("Seleccione uno o más archivos JSON para cargar (separados por comas):")
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")

        file_indices = input("Ingrese los números de los archivos: ").split(',')

        # Validar y convertir los índices ingresados
        try:
            file_indices = [int(index.strip()) - 1 for index in file_indices]
        except ValueError:
            print("Entrada inválida.")
            return

        # Procesar los archivos seleccionados
        for file_index in file_indices:
            if file_index < 0 or file_index >= len(files):
                print(f"Selección inválida: {file_index + 1}")
                continue

            selected_file = files[file_index]
            file_path = os.path.join(assets_folder, selected_file)
            procesar_archivo(file_path)

    elif opcion == "2":
        # Opción 2: Dibujar todas las imágenes
        for selected_file in files:
            file_path = os.path.join(assets_folder, selected_file)
            procesar_archivo(file_path)

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()