import json      # Módulo para manejar archivos JSON
import time      # Módulo para controlar el tiempo (delay)
import random    # Módulo para generar valores aleatorios

# Ruta al archivo JSON donde se encuentran los datos de los pozos
archivo_json = 'datos.json'

# Se inicializa un vector con 20 estados "Activo" (uno por cada pozo)
vector_estados = ["Activo"] * 20  # Lista que representa el estado de cada pozo

# Función que actualiza los estados de los pozos en el archivo JSON
def actualizar_estados(vector):
    # Abrir el archivo JSON en modo lectura
    with open(archivo_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)  # Cargar los datos del archivo como una lista de diccionarios

    # Recorrer el vector de estados y actualizar el correspondiente en los datos del archivo
    for i, estado in enumerate(vector):
        nombre_pozo = f"Pozo {i+1}"  # Formato del nombre del pozo: "Pozo 1", "Pozo 2", etc.
        for pozo in datos:
            if pozo["nombre"] == nombre_pozo:
                pozo["estado"] = estado  # Actualizar el estado del pozo si coincide el nombre
                break  # Salir del bucle interno al encontrar el pozo

    # Guardar los datos actualizados en el mismo archivo JSON
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)  # Guardar con indentado para legibilidad

    print("Estados actualizados")  # Mensaje de confirmación en consola
    return

# Lista de estados posibles que puede tomar cada pozo
estados_posibles = ["Activo", "Inactivo", "Emergencia", "En mantenimiento"]

# Bucle infinito para actualizar los estados cada 10 segundos
while True:
    actualizar_estados(vector_estados)  # Llama a la función para actualizar el archivo JSON

    time.sleep(10)  # Espera 10 segundos antes de la próxima actualización

    # Se genera un nuevo vector de estados aleatorios para la siguiente iteración
    vector_estados = [random.choice(estados_posibles) for _ in range(20)]
