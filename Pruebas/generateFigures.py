import json
import random
import os
from datetime import datetime

def generate_random_color():
    return {
        "red": random.randint(0, 255),
        "green": random.randint(0, 255),
        "blue": random.randint(0, 255)
    }

def generate_random_point(scene_size):
    # Genera un punto aleatorio dentro del tamaño de la escena
    x = random.randint(0, scene_size["width"] - 1)  # El punto no puede exceder el ancho
    y = random.randint(0, scene_size["height"] - 1)  # El punto no puede exceder la altura
    return {"x": x, "y": y}

def generate_random_size():
    return {"width": random.randint(50, 500), "height": random.randint(50, 500)}


def generate_random_figure(fig_id, scene_size):
    figure_types = ["ellipse", "circle", "triangle", "rectangle", "square", "polygon"]
    fig_type = random.choice(figure_types)
    
    figure = {
        "id": fig_id,
        "type": fig_type,
        "color": generate_random_color()
    }
    
    if fig_type in ["polygon", "triangle"]:
        # Para polígonos y triángulos, generamos varios puntos
        figure["points"] = [generate_random_point(scene_size) for _ in range(random.randint(3, 6))]
    elif fig_type == "circle":
        # Para círculos, generamos un centro y un radio
        figure["points"] = {
            "center": generate_random_point(scene_size),
            "radius": random.randint(10, 100)
        }
    elif fig_type == "ellipse":
        # Para elipses, generamos un centro y dos radios
        figure["points"] = {
            "center": generate_random_point(scene_size),
            "radii": generate_random_size()
        }
    elif fig_type == "square":
        # Para cuadrados, generamos el punto superior izquierdo y el lado
        figure["points"] = {
            "topleft": generate_random_point(scene_size),
            "side": random.randint(10, 200)
        }
    elif fig_type == "rectangle":
        # Para rectángulos, generamos el punto superior izquierdo y las dimensiones del lado
        figure["points"] = {
            "topleft": generate_random_point(scene_size),
            "sides": generate_random_size()
        }
    
    return figure


def generate_relations(num_figures):
    relations = []
    if num_figures > 1:
        ids = list(range(1, num_figures + 1))  #IDs consecutivos
        random.shuffle(ids)  # aleatorio entre las figuras
        for i in range(num_figures - 1):
            relations.append({"obj1": ids[i], "obj2": ids[i + 1]})  # Relación entre figuras consecutivas
    return relations


def generate_scene(num_figures):
    scene_size = generate_random_size()
    
    # Generamos los objetos (figuras) pasándoles el tamaño de la escena
    scene = {
        "size": scene_size,
        "background": generate_random_color(),
        "objects": [generate_random_figure(i, scene_size) for i in range(1, num_figures + 1)],
        "relations": generate_relations(num_figures)
    }

    return {"scene": scene}


def main():
    num_files = int(input("Ingrese la cantidad de archivos a generar: "))
    num_figures = int(input("Ingrese la cantidad de figuras por archivo (máx 7): "))
    num_figures = min(num_figures, 7)
    
    folder_name = f"{num_figures}Figuras"
    os.makedirs(folder_name, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    for i in range(num_files):
        scene = generate_scene(num_figures)
        filename = os.path.join(folder_name, f"figures{timestamp}_{i+1}.json")
        with open(filename, "w") as f:
            json.dump(scene, f, indent=4)
        print(f"Archivo generado: {filename}")

if __name__ == "__main__":
    main()
