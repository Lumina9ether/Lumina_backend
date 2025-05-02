from flask import Flask, request, jsonify, render_template
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_text}]
    )
    return jsonify({"response": response.choices[0].message["content"]})

if __name__ == "__main__":
    app.run(debug=True)
