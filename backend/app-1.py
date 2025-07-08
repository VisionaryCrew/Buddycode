from flask import Flask, request, jsonify
from flask_cors import CORS
from model_api import generate_code

app = Flask(__name__, static_folder="../frontend", static_url_path="/static")
CORS(app)  # Enables cross-origin support for frontend JS

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_logic = data.get("logic", "").strip()

    if not user_logic:
        return jsonify({"response": "⚠️ No logic provided. Please write your logic clearly."}), 400

    generated_output = generate_code(user_logic)
    return jsonify({"response": generated_output})

if __name__ == "__main__":
    app.run(debug=True)
