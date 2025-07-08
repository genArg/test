# Importamos módulos necesarios
import os                                # Para obtener variables de entorno como el puerto
from flask import Flask, jsonify, send_from_directory

# Creamos la app Flask, y especificamos que la carpeta estática es la raíz del proyecto (donde están los archivos .html, .js, .css)
app = Flask(__name__, static_folder=".")

# Datos simulados de los pozos
pozos = [
    {
        "nombre": "Pozo A",
        "lat": -26.8241,
        "lng": -65.2226,
        "estado": "Activo"
    },
    {
        "nombre": "Pozo B",
        "lat": -26.8300,
        "lng": -65.2300,
        "estado": "En mantenimiento"
    },
    {
        "nombre": "Pozo C",
        "lat": -26.8150,
        "lng": -65.2100,
        "estado": "Emergencia"
    }
]

# Ruta principal: envía el archivo HTML principal
@app.route("/")
def home():
    return send_from_directory(".", "index.html")  # Devuelve index.html desde la raíz del proyecto

# Ruta para la hoja de estilos
@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

# Ruta para el archivo JavaScript
@app.route("/main.js")
def js():
    return send_from_directory(".", "main.js")

# Ruta para devolver los datos en formato JSON
@app.route("/datos.json")
def datos():
    return send_from_directory(".", "datos.json")

# Punto de entrada principal de la app
if __name__ == "__main__":
    # Render define el puerto a través de la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))  # Si no está definida, usa el puerto 5000 por defecto

    # Ejecuta la app en 0.0.0.0 (permite acceso externo) y en el puerto indicado
    app.run(host="0.0.0.0", port=port)
