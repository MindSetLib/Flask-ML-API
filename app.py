import os

# from insolver import InsolverDataFrame
# from insolver.transforms import InsolverTransform, load_transforms
# from insolver.wrappers import InsolverGLMWrapper, InsolverGBMWrapper
# from insolver.serving import utils

from flask import Flask, request, jsonify


# For logging
import logging
import traceback
from logging.handlers import RotatingFileHandler
from time import strftime, time

app = Flask(__name__)

# Logging
handler = RotatingFileHandler('logs/app.log', maxBytes=100000, backupCount=5)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


# model initization
# model_path = os.environ['model_path']
# transforms_path = os.environ['transforms_path']

# model = utils.load_pickle_model(model_path) 


@app.route("/")
def index():
    return "API for predict service"


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    # Request logging
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    logger.info(f'{current_datatime} request from {ip_address}: healthcheck')

    return jsonify({'status': 'ok'})


@app.route("/predict", methods=['POST'])
def predict():
    # json_input = request.json

    # Request logging
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    # ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    # logger.info(f'{current_datatime} request from {ip_address}: {request.json}')
    start_prediction = time()

    result = {
        'status': 'ok',
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
