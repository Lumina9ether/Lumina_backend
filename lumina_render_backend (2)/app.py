from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-..."

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")
    print("User said:", user_text)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Lumina, a cosmic AI assistant."},
            {"role": "user", "content": user_text}
        ]
    )

    lumina_reply = response.choices[0].message.content
    return jsonify({"reply": lumina_reply})
