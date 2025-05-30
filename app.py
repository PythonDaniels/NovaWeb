from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Permitir CORS solo desde tu frontend en Netlify
CORS(app, resources={r"/formulario": {"origins": "https://nova-webb.netlify.app"}})

@app.route('/formulario', methods=['POST'])
def recibir_formulario():
    data = request.json
    print("Datos recibidos:", data)
    return jsonify({"mensaje": "Formulario recibido correctamente"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
