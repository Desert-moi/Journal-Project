# Based on the LING508 Sanskrit example project, https://github.com/jjberry-508/sanskrit-508

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from app.services import Services


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/get_data": {"origins": 'http://localhost:port'}})

services = Services()


@app.route("/get_data/<string:author>", methods=["GET"])
@cross_origin(origin='http://localhost:5000', headers=['Content-Type', 'Authorization'])
def get_data(author):

    data = services.recall_author(author)

    if not data:
        return jsonify({"error": "No journals found for the given author"}), 404

    # Convert JournalEntry objects to dictionaries for JSON response
    result = [entry.__dict__ for entry in data]

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
