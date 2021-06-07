import sys
import json
import requests
from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
sys.path.append('.')
from daily_code.logger import get_logger
from daily_code.apis.corona import api
from daily_code.config import CoronaServerUrl



namespace = Namespace("endpoints", description="endpoint for corona actions")

logger = get_logger("corona-api")

parser = api.parser()

#parser.add_argument("user id", type=str, required=True, location="form")
parser.add_argument("data", type=dict, required=True, location="form")

@namespace.route("/", methods=["POST"])
@namespace.expect(parser)
class MyEndpoint(Resource):
    @namespace.doc("send data request to corona server")
    def post(self):
        logger.debug(f'got post request')
        
        payload = request.form

        url = CoronaServerUrl + "/endpoints/input/"

        data = json.loads(payload['data'])

        

        res = requests.post(url, json={"payload":data})
        
        return res.text

        # do stuff here

