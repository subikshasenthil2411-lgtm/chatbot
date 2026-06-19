from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder="static")
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2"

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    system_prompt = data.get("system", "You are a helpful personal assistant. Be friendly, concise, and practical.")

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    try:
        full_messages = [{"role": "system", "content": system_prompt}] + messages

        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "messages": full_messages,
            "stream": False
        })

        result = response.json()
        reply = result["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"Make sure Ollama is running! Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)