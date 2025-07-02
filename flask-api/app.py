from flask import Flask, request, jsonify
from datetime import datetime
import textblob

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Text is required"}), 400

    blob = textblob.TextBlob(text)
    sentiment = blob.sentiment.polarity

    return jsonify({
        "input": text,
        "sentiment": "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral",
        "timestamp": datetime.now()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
