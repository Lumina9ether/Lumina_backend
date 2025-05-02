
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-your-backup-openai-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")
    print("User said:", user_text)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_text}]
    )
    reply = response.choices[0].message.content.strip()
    return jsonify({"response": reply})
