#!/usr/bin/python3
"""Flask RESTful application"""
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def error_404(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown(self):
    """Close the storage"""
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") or "0.0.0.0"
    port = getenv("HBNB_API_PORT") or 5000
    app.run(host=host, port=port, threaded=True)
