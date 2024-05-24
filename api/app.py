import base64
import json

from cryptography.fernet import Fernet
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.get("/key")
def get_key():
    key = Fernet.generate_key()
    user = request.args.get('user')

    with open("db.json", "r+") as db:  # Open in read/write mode
        file = json.load(db)
        file[user] = base64.urlsafe_b64encode(key).decode()  # Decode key to string before storing

        # Move to the beginning before writing (not strictly necessary in this case)
        db.seek(0)
        json.dump(file, db)

    return key


@app.get("/key/<username>")
def get_key_by_username(username):
    with open("db.json") as db:
        data = json.load(db)
    key = data[username]
    return base64.urlsafe_b64decode(key)


@app.get("/keys")
def get_keys():
    with open("db.json") as db:
        return json.load(db)  # Return the entire data dictionary


@app.route('/creds', methods=['POST', 'GET'])
@cross_origin()
def cred():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        with open("creds.json", "r+") as db:
            file = json.load(db)
            file[username] = password
            db.seek(0)
            json.dump(file, db)
        return {username: password}
    elif request.method == 'GET':
        with open("creds.json") as db:
            return json.load(db)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
