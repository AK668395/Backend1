
from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

# Reads your Gemini API key from an environment variable
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Set it in CMD before running."
    )

client = genai.Client(api_key=api_key)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get('message', '')

    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({"error": "Message is required"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        return jsonify({
            "user_message": user_message,
            "ai_response": response.text
        })

    except Exception:
        app.logger.exception("Gemini API request failed")
        return jsonify({
            "error": "Failed to generate a response. Check the server logs."
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
