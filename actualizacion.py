import json
import time
import random

# Ruta al archivo JSON
archivo_json = 'datos.json'

# Simulación de vector de estados (puede cambiarse dinámicamente)
# Por ejemplo: ["Activo", "Inactivo", ...] con 20 elementos
vector_estados = ["Activo"] * 20  # Inicializa todos como "Activo"

def actualizar_estados(vector):
    with open(archivo_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    for i, estado in enumerate(vector):
        nombre_pozo = f"Pozo {i+1}"
        for pozo in datos:
            if pozo["nombre"] == nombre_pozo:
                pozo["estado"] = estado
                break

    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    print("Estados actualizados")

estados_posibles = ["Activo", "Inactivo", "Emergencia", "En mantenimiento"]
# Bucle principal que actualiza cada 10 segundos
while True:
    # (acá podrías actualizar dinámicamente el vector_estados si lo necesitás)
    actualizar_estados(vector_estados)
    time.sleep(10)
    vector_estados = [random.choice(estados_posibles) for _ in range(20)]
