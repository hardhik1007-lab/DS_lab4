from flask import Flask, jsonify
import requests

app = Flask(__name__)
USER_SERVICE_URL = "http://user-service:5000"

@app.route("/greet/<int:user_id>")
def greet(user_id):
    try:
        user = requests.get(f"{USER_SERVICE_URL}/user/{user_id}").json()
        if "error" in user:
            return jsonify({"message": "User not found"})
        return jsonify({"message": f"Hello {user['name']}!"})
    except Exception as e:
        return jsonify({"message": "User-service unavailable", "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)