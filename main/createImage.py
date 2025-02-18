from PIL import Image, ImageDraw
import json
import os


from utils import get_color,generar_nombre_archivo, get_carpeta

# Cargar el archivo JSON
with open('scene.json', 'r') as f:
    scene = json.load(f)

# Crear una imagen con el tamaño y color de fondo especificados
width = scene['size']['width']
height = scene['size']['height']
background_color = get_color(scene['background'])
imagen = Image.new('RGB', (width, height), background_color)
dibujo = ImageDraw.Draw(imagen)

# Dibujar cada objeto en la escena
for obj in scene['objects']:
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
nombre_archivo=generar_nombre_archivo("imagen", "png")
ruta = get_carpeta('imagenes',nombre_archivo)

# Guardar la imagen generada
imagen.save(ruta)
print(f"Guardado en la carpeta imagenes como: {nombre_archivo}")