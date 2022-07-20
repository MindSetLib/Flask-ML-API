from time import strftime, time
import os
import logging
import traceback

from dotenv import load_dotenv

from insolver import InsolverDataFrame
from insolver.transforms import InsolverTransform, load_transforms
from insolver.wrappers import InsolverGLMWrapper, InsolverGBMWrapper
from insolver.serving import utils

from flask import Flask, request, jsonify

import pandas as pd

# load dotenv data
load_dotenv()

app = Flask(__name__)

# Logging
handler = logging.StreamHandler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


# model initization
model_path = os.environ.get('model_path')
transforms_path = os.environ.get('transforms_path')

model = utils.load_pickle_model(model_path) 
if model and model.algo == 'gbm':
    model = InsolverGBMWrapper(backend=model.backend, load_path=model_path)
elif model and model.algo == 'glm':
    model = InsolverGLMWrapper(backend='sklearn', load_path=model_path)
else:
    model = InsolverGLMWrapper(backend='h2o', load_path=model_path)

# load transformations
tranforms = load_transforms(transforms_path)


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    # Request logging
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    logger.info(f'{current_datatime} request from {ip_address}: healthcheck')

    return jsonify({'status': 'ok'})


@app.route("/predict", methods=['POST'])
def predict():
    # Request logging
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    logger.info(f'{current_datatime} request from {ip_address}: {request.json}')
    start_prediction = time()

    # json request
    data_dict = request.json
    df = pd.DataFrame(data_dict['df'], index=[0])
    insdataframe = InsolverDataFrame(df)
    # Apply transformations
    instransforms = InsolverTransform(insdataframe, tranforms)
    instransforms.ins_transform()

    # Prediction
    predicted = model.predict(instransforms)

    result = {
        'predicted': predicted.tolist()
    }

    # Response logging
    end_prediction = time()
    duration = round(end_prediction - start_prediction, 6)
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    logger.info(f'{current_datatime} predicted for {duration} msec: {result}\n')

    return jsonify(result)


@app.errorhandler(Exception)
def exceptions(e):
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    error_message = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                 current_datatime,
                 request.remote_addr,
                 request.method,
                 request.scheme,
                 request.full_path,
                 error_message)
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
