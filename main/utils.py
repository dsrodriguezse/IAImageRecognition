from datetime import datetime
import os


# Función para generar el nombre del archivo con fecha y hora
def generar_nombre_archivo(base_name, extension):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # Formato: AñoMesDía_HoraMinutoSegundo
    return f"{base_name}_{timestamp}.{extension}"

def generar_nombre_archivo(base_name, suffix, extension):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # Formato: AñoMesDía_HoraMinutoSegundo
    return f"{base_name}_{suffix}_{timestamp}.{extension}"

# ruta carpetas JSON/imagenes
def get_carpeta(tipo,nombre_archivo):
    return os.path.join('..', tipo, nombre_archivo)

# Función para convertir el color del JSON a una tupla RGB
def get_color(color_dict):
    return (color_dict['red'], color_dict['green'], color_dict['blue'])

# Colores permitidos y sus valores RGB
COLORES_PERMITIDOS = {
    "amarillo": {"red": 255, "green": 255, "blue": 0},
    "rojo": {"red": 255, "green": 0, "blue": 0},
    "azul": {"red": 0, "green": 0, "blue": 255},
    "negro": {"red": 0, "green": 0, "blue": 0},
    "verde": {"red": 0, "green": 255, "blue": 0},
    "blanco": {"red": 255, "green": 255, "blue": 255}
}

# Función para convertir un color RGB a un diccionario
def get_color_dict(rgb):
    return {'red': rgb[0], 'green': rgb[1], 'blue': rgb[2]}
