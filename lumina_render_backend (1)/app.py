from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    user_text = data.get("text", "")
    print("User said:", user_text)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Lumina, a high-vibrational AI assistant who inspires, educates, and empowers users to achieve success."},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Sorry, I had trouble processing that."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)