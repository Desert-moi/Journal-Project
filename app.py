# Based on the LING508 Sanskrit example project, https://github.com/jjberry-508/sanskrit-508

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from app.services import Services


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/get_data": {"origins": 'http://localhost:3000'}})

services = Services()


@app.route("/get_data", methods=["GET"])  # Add URL here, after "/" (e.g. "/get_data")
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])
def get_data():
    author = request.args.get('author')
    if not author:
        return jsonify({"error": "No author provided"}), 400

    data = services.recall_author(author)
    return jsonify({"result": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
