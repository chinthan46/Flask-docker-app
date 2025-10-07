from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def hello():
    logger.info("Root endpoint was called")
    return jsonify({"message": "Hello from Flask + Docker!"})

@app.route("/health")
def health():
    logger.info("Health endpoint was checked")
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
