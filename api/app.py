# app.py
import json

from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)


@app.get("/key")
def get_key():
    key = Fernet.generate_key()
    user = request.args.get('user')
    data = {
        user: str(key)
    }
    with open("db.json") as db:
        file = json.load(db)
    file.upda
    with open("db.json", 'a+') as db:
        json.dump(data, db)

    return key


@app.get("/keys")
def get_keys():
    with open("db.json") as db:
        data = json.load(db)
    return data


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

"""@app.post("/data")
def post_data():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
"""
