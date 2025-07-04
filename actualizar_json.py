import json      # Módulo para manejar archivos JSON

def convertir_vector(vector_inicial):
    # Ruta al archivo JSON donde se encuentran los datos de los pozos
    archivo_json = 'datos.json'

    # Inicializa el vector de salida con todos "Activo"
    vector = ["Activo"] * 20

    # Itera sobre los 20 elementos del vector
    for i in range(20):
        # Estructura match-case para asignar estado según valor
        match vector_inicial[i]:
            case 0:
                vector[i] = "Inactivo"
            case -1:
                vector[i] = "Emergencia"
            case _:
                vector[i] = "Activo"  # Por defecto, se considera "Activo"
    
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

    # Imprime el resultado (opcional)
    #print(vector)

    # Devuelve el vector final
    return
