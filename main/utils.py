from datetime import datetime

# Función para generar el nombre del archivo con fecha y hora
def generar_nombre_archivo(base_name, extension):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # Formato: AñoMesDía_HoraMinutoSegundo
    return f"{base_name}_{timestamp}.{extension}"

# Función para convertir el color del JSON a una tupla RGB
def get_color(color_dict):
    return (color_dict['red'], color_dict['green'], color_dict['blue'])

# Función para convertir un color RGB a un diccionario
def get_color_dict(rgb):
    return {'red': rgb[0], 'green': rgb[1], 'blue': rgb[2]}
