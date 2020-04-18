from flask import Flask, request, jsonify
import h2o

from process_data import process_input

app = Flask(__name__)

h2o.init()
model_glm_poisson = h2o.load_model('models/GLM_model_python_1573818197972_1')
model_glm_gamma = h2o.load_model('models/GLM_model_python_1573818197972_2')


@app.route("/")
def index():
    return "API for predict service"


@app.route("/predict", methods=['POST'])
def predict():

    json_input = request.json

    id = json_input['ID']
    hf = process_input(json_input)

    prediction_Poisson = model_glm_poisson.predict(hf)
    value_Poisson = prediction_Poisson.as_data_frame()['predict'][0]

    prediction_Gamma = model_glm_gamma.predict(hf)
    value_Gamma = prediction_Gamma.as_data_frame()['predict'][0]

    value_BurningCost = value_Poisson * value_Gamma

    result = {
        'ID': id,
        'value_Poisson': value_Poisson,
        'value_Gamma': value_Gamma,
        'value_BurningCost': value_BurningCost
        }

    return jsonify(result)


@app.errorhandler(Exception)
def exceptions(e):
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
