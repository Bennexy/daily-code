import sys
import requests
import datetime
from flask_restx import Namespace, Resource, fields
from flask import json, jsonify, request
sys.path.append('.')
from daily_code.logger import get_logger
from daily_code.apis.db import api



namespace = Namespace("endpoints", description="endpoint for db actions")

logger = get_logger("db-api")

parser_in = api.parser()

parser_in.add_argument("datatype", type=dict, required=True, location="form")
parser_in.add_argument("data", type=dict, required=True, location="form")

@namespace.route("/")
@namespace.expect(parser_in)
class MyEndpoint(Resource):
    @namespace.doc("uploads data to db")
    def post(self):
        payload = request.form

        datatype = payload['datatype']
        data = payload['data']

        date = datetime.datetime.now().strftime("%Y/%m/%d")

        # do stuff here