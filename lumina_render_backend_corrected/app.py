from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-REPLACE_THIS_WITH_YOUR_KEY"

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Lumina, a wise and interactive AI assistant."},
            {"role": "user", "content": user_text}
        ]
    )

    return jsonify({"response": response.choices[0].message["content"]})

@app.route("/")
def home():
    return render_template("index.html")