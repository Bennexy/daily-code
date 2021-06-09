import sys
import requests
import datetime
from flask_restx import Namespace, Resource, fields
from flask import json, jsonify, request
sys.path.append('.')
from daily_code.logger import get_logger
from daily_code.apis.db import api
from daily_code.apis.db.errors import UnknownDataType
from daily_code.apis.db.tasks.corona_db_actions import add_entry



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
        
        try:
            payload = request.json
            datatype = payload['datatype']
            data = payload['data']
            return jsonify(message=f"recieved post to upload datatype {datatype} data {data} to db")

        except KeyError as e:
            datatype = None
            data = None
            logger.error(f'an KeyError has occured within the post to db api endpoint - could not provide data and datatype within payload {payload}')
            return jsonify(f"a KeyError {e} has occured. Please provide the datatype and the data in json format")

        finally:
            date = datetime.datetime.now().strftime("%Y/%m/%d")
            if data != None and datatype != None:
                
                if datatype == "corona":
                    logger.debug(f"uploading data of the datatype {datatype} to db")
                    for _, data_base in data.items():
                        for _, ort_data in data_base.items():
                            add_entry(ort_data)

                else:
                    logger.error(f"datatype {datatype} is not known to db api")
                    raise UnknownDataType(f"datatype {datatype} is not known to db api")