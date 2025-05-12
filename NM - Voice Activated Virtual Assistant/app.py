from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import openai, os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def process():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "Can you repeat that?"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if enabled
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Something went wrong. Try again later."})

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    app.run(debug=True)
