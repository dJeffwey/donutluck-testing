from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "service": "DonutLuck Security Testing",
        "time": datetime.now(timezone.utc).isoformat()
    })

@app.route("/health")
def health():
    return jsonify({"healthy": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
