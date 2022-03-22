from flask import Flask, jsonify
from usuarios import usuarios

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"response": "hola mundo"})

@app.route('/usuarios')
def getUsuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)