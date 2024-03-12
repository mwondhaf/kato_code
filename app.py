from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib


app = Flask(__name__)
CORS(app)

users = [{'id': 1, 'name': "Alice"}, {'id': 2, 'name': "Bob"}, {'id': 3, 'name': "Charlie"}]

# editor 
@app.route("/users", methods=['GET', 'POST'])
def handle_users():
    global users

    if request.method == 'GET':
        return jsonify(users)

    if request.method == 'POST':
        data = request.json
        if 'name' and 'password' in data:

            hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()

            new_user = {'id': len(users) + 1, 'name': data['name'], 'password': hashed_password}
            users.append(new_user)

            # save in the database 

            return jsonify(users), 201
        else:
            return "Name not provided", 400

if __name__ == "__main__":
    app.run(debug=True)
