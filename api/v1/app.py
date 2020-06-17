#!/usr/bin/python3
""" Flask - PyMongo App """

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.auth import app_auth
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(app_views)
app.register_blueprint(app_auth)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(404)
def not_fount(error):
    """ 404 error """
    return make_response(jsonify({'status': "Not found"}), 404)

if __name__ == "__main__":
    host_api = os.getenv("HAANA_HOST_API", "0.0.0.0")
    port_api = os.getenv("HAANA_PORT_API", "5000")
    app.run(host=host_api, port=port_api, threaded=True, debug=True)
