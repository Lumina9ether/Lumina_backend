from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import elevenlabs
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs.set_api_key(os.getenv("ELEVENLABS_API_KEY"))

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")
    return jsonify({"response": f"You said: {user_text}"})
