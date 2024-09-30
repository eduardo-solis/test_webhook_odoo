from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hola mundo</h1>"

@app.route("/ping")
def pong():
    return "<h1>pong!</h1>"

@app.route("/my_webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        try:
            data = request.get_json()
            print(f"Data > \n{data}")
            return jsonify({
                "status": "success",
                "message": "Datos procesados correctamente",
                "received_data": data
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"{e}"
            }), 400
    return jsonify({
                "status": "error",
                "message": "Metodo no permitido"
            }), 405

