from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return "API for predict service"


@app.route("/predict", methods=['POST'])
def predict():

    json_input = request.json

    id = json_input['ID']

    result = {
        'ID': id,
        'result': 'prediction'
        }

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
