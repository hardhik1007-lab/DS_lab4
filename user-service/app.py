from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/<int:user_id>")
def get_user(user_id):
    data = {
        1: {"id": 1, "name": "Hardhik", "role": "student"},
        2: {"id": 2, "name": "Messi", "role": "lecturer"}
    }
    return jsonify(data.get(user_id, {"error": "User not found"}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)