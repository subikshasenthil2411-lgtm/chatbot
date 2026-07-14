from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__, static_folder="static")
CORS(app)

client = Groq()

MODEL_NAME = os.environ.get("MODEL_NAME", "llama-3.3-70b-versatile")
DEFAULT_SYSTEM_PROMPT = "You are a helpful personal assistant for all users. Be friendly, concise, and practical."


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])
    system_prompt = data.get("system", DEFAULT_SYSTEM_PROMPT)

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    try:
        full_messages = [{"role": "system", "content": system_prompt}] + messages
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=full_messages,
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"Groq API error: {str(e)}"}), 502


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
