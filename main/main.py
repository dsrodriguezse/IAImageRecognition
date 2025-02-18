from createImage import crear_imagen
from createJson import crear_json

# Generar una imagen desde un JSON
crear_imagen('scene.json', 'output_scene.png')


# Generar un JSON desde la imagen
#crear_json('output_scene.png', 'detected_scene.json')