import base64
import json

from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flasgger import Swagger

app = Flask(__name__)
CORS(app)
swagger = Swagger(app, template={
    "info": {
        "title": "Ransomware Simulator API",
        "description": "An educational API for interacting with the Ransomware Simulator",
        "version": "1.0.0"
    }
})

@app.get("/key")
def get_key():
    """
    Generates a new Fernet key, associates it with a user, and stores it in db.json.
    ---
    responses:
        200:
            description: A successful response
            examples:
                application/json: "generated_key"
    """
    key = Fernet.generate_key()
    user = request.args.get('user')

    try:
        with open("db.json", "r+") as db:
            # Load existing data
            file = json.load(db)
            # Store the new key for the user
            file[user] = base64.urlsafe_b64encode(key).decode()

            # Reset the file and write updated data
            db.seek(0)
            db.truncate()
            json.dump(file, db, indent=4)

        return key
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.get("/key/<username>")
def get_key_by_username(username):
    """
    Retrieves the Fernet key associated with a given username from db.json.
    ---
    parameters:
      - name: username
        in: path
        description: The username whose key needs to be retrieved
        required: true
        schema:
          type: string
    responses:
        200:
            description: A successful response
            examples:
                application/json: "retrieved_key"
        404:
            description: User not found
            examples:
                application/json: {"error": "User not found"}
    """
    try:
        with open("db.json") as db:
            data = json.load(db)
        key = data.get(username)
        if key:
            return base64.urlsafe_b64decode(key)
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.get("/keys")
def get_keys():
    """
    Returns all user-key pairs stored in db.json.
    ---
    responses:
        200:
            description: A successful response
            examples:
                application/json: {"user1": "key1", "user2": "key2"}
    """
    try:
        with open("db.json") as db:
            return jsonify(json.load(db))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/creds', methods=['POST', 'GET'])
@cross_origin(allow_headers=['Content-Type'])
def cred():
    """
    Handles both storing and retrieving user credentials in/from creds.json.
    ---
    responses:
        200:
            description: A successful response
            examples:
                application/json: {"username": "password"}
    """
    if request.method == 'POST':
        try:
            username = request.json['username']
            password = request.json['password']
            with open("creds.json", "r+") as db:
                # Load existing credentials
                file = json.load(db)
                # Store the new credentials
                file[username] = password

                # Reset the file and write updated data
                db.seek(0)
                db.truncate()
                json.dump(file, db, indent=4)
            return jsonify({username: password})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'GET':
        try:
            with open("creds.json") as db:
                return jsonify(json.load(db))
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/cred/<username>', methods=['GET'])
def get_cred(username):
    """
    Retrieves the password associated with the given username from creds.json.
    ---
    parameters:
      - name: username
        in: path
        description: The username whose password needs to be retrieved
        required: true
        schema:
          type: string
    responses:
        200:
            description: A successful response
            examples:
                application/json: {"username": "password"}
        404:
            description: User not found
            examples:
                application/json: {"error": "User not found"}
    """
    try:
        with open("creds.json") as db:
            data = json.load(db)
        password = data.get(username)
        if password:
            return jsonify({username: password})
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode on port 5000
    app.run(host="0.0.0.0", port=5000)
