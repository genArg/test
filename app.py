from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder=".")

# Datos simulados (antes estaban en datos.json)
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

# Rutas para archivos estáticos
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

@app.route("/main.js")
def js():
    return send_from_directory(".", "main.js")

# Ruta nueva: devuelve datos en formato JSON
#@app.route("/api/pozos")
#def api_pozos():
#    return jsonify(pozos)

@app.route("/datos.json")
def datos():
    return send_from_directory(".", "datos.json")

if __name__ == "__main__":
    app.run(debug=True)
