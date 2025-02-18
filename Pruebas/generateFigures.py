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

def generate_random_point():
    return {"x": random.randint(0, 500), "y": random.randint(0, 500)}

def generate_random_size():
    return {"width": random.randint(10, 200), "height": random.randint(10, 200)}

def generate_random_figure(fig_id):
    figure_types = ["ellipse", "circle", "triangle", "rectangle", "square", "polygon"]
    fig_type = random.choice(figure_types)
    
    figure = {
        "id": fig_id,
        "type": fig_type,
        "color": generate_random_color()
    }
    
    if fig_type in ["polygon", "triangle"]:
        figure["points"] = [generate_random_point() for _ in range(random.randint(3, 6))]
    elif fig_type == "circle":
        figure["points"] = {"center": generate_random_point(), "radius": random.randint(10, 100)}
    elif fig_type == "ellipse":
        figure["points"] = {"center": generate_random_point(), "radii": generate_random_size()}
    elif fig_type == "square":
        figure["points"] = {"topleft": generate_random_point(), "side": random.randint(10, 200)}
    elif fig_type == "rectangle":
        figure["points"] = {"topleft": generate_random_point(), "sides": generate_random_size()}
    
    return figure

def generate_relations(num_figures):
    relations = []
    if num_figures > 1:
        ids = list(range(1, num_figures + 1))
        random.shuffle(ids)
        for i in range(num_figures - 1):
            relations.append({"obj1": ids[i], "obj2": ids[i + 1]})
    return relations

def generate_scene(num_figures):
    scene = {
        "size": generate_random_size(),
        "background": generate_random_color(),
        "objects": [generate_random_figure(i) for i in range(1, num_figures + 1)],
        "relations": [generate_relations(num_figures)]  # Puedes agregar lógica para relaciones si lo deseas
    }
    return scene

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
