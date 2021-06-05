import sys
import requests
from flask_restx import Namespace, Resource, fields
from flask import json, jsonify, request
sys.path.append('.')
from daily_code.logger import get_logger
from daily_code.apis.corona import api



namespace = Namespace("endpoints", description="endpoint for corona actions")

logger = get_logger("corona-api")

parser = api.parser()

parser.add_argument("user id", type=str, required=True, location="form")
parser.add_argument("data", type=str, required=True, location="form")

@namespace.route("/", methods=["POST"])
@namespace.expect(parser)
class MyEndpoint(Resource):
    #@namespace.doc("send data request to corona server")
    def post(self):
        payload = request.form
        

        # do stuff here

