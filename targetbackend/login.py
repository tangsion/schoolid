
from flask import Flask, request, jsonify
from db import get_db

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
@app.route('/login', methods=['POST'])
def login():
    print("🔥 login 被调用了")
    return jsonify({"msg": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
