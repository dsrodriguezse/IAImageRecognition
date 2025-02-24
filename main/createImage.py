from PIL import Image, ImageDraw
import json
import os

from utils import get_color, generar_nombre_archivo, get_carpeta

# Listar archivos en la carpeta "assets"
assets_folder = 'assets'
files = [f for f in os.listdir(assets_folder) if f.endswith('.json')]

if not files:
    print("No se encontraron archivos JSON en la carpeta 'assets'.")
    exit()

# Mostrar archivos y pedir al usuario que seleccione uno
print("Seleccione un archivo JSON para cargar:")
for i, file in enumerate(files):
    print(f"{i + 1}. {file}")

file_index = int(input("Ingrese el número del archivo: ")) - 1

if file_index < 0 or file_index >= len(files):
    print("Selección inválida.")
    exit()

selected_file = files[file_index]
file_path = os.path.join(assets_folder, selected_file)

# Cargar el archivo JSON seleccionado
with open(file_path, 'r') as f:
    scene = json.load(f)

# Acceder a la clave 'scene' dentro del archivo JSON
scene_data = scene['scene']

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

# Nombre archivo en carpeta imagenes
json_filename = os.path.splitext(selected_file)[0]
suffix = json_filename[-5:]
nombre_archivo = generar_nombre_archivo("imagen",suffix, "png")
ruta = get_carpeta('imagenes', nombre_archivo)

# Guardar la imagen generada
imagen.save(ruta)
print(f"Guardado en la carpeta imagenes como: {nombre_archivo}")