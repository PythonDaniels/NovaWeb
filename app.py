from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para permitir conexión desde Netlify

@app.route('/formulario', methods=['POST'])
def recibir_formulario():
    data = request.json
    print("Datos recibidos:", data)
    return jsonify({"mensaje": "Formulario recibido correctamente"}), 200

if __name__ == '__main__':
    app.run()