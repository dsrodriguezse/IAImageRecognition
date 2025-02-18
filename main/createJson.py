from PIL import Image
import json
import os


from utils import get_color_dict,generar_nombre_archivo, get_carpeta

# Cargar la imagen
imagen = Image.open('output_scene.png')
pixeles = imagen.load()

# Detectar figuras (esto es un ejemplo básico)
objects = []
for y in range(0, imagen.height, 10):  # Escaneo cada 10 píxeles para simplificar
    for x in range(0, imagen.width, 10):
        color_pixel = pixeles[x, y]
        if color_pixel != (255, 255, 255):  # Ignorar el fondo blanco
            objects.append({
                'id': len(objects) + 1,
                'type': 'circle',  # Aquí deberías detectar el tipo de figura
                'color': get_color_dict(color_pixel),
                'points': {
                    'center': {'x': x, 'y': y},
                    'radius': 10  # Radio fijo para simplificar
                }
            })

# Crear el JSON
scene = {
    'size': {'width': imagen.width, 'height': imagen.height},
    'background': {'red': 255, 'green': 255, 'blue': 255},
    'objects': objects,
    'relations': []  # Aquí podrías detectar relaciones entre objetos
}

# Nombre archivo en carpetea JSON
nombre_archivo = generar_nombre_archivo("figuras", "json")
ruta = get_carpeta('JSON',nombre_archivo)

# Guardar el JSON
with open(ruta, 'w') as f:
    json.dump(scene, f, indent=4)
print(f"Guardado en la carpeta JSON como: {nombre_archivo}")
