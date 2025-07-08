from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.model_api import generate_code



# Define app with static frontend path
app = Flask(__name__, static_folder="../frontend", static_url_path="/static")
CORS(app)  # Enables cross-origin support

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_logic = data.get("logic", "").strip()

    if not user_logic:
        return jsonify({
            "response": {
                "reasoning": "⚠️ No logic provided.",
                "code": "",
                "edge_cases": ""
            }
        }), 400

    generated_output = generate_code(user_logic)

    if isinstance(generated_output, str):
        return jsonify({
            "response": {
                "reasoning": generated_output,
                "code": "",
                "edge_cases": ""
            }
        })

    return jsonify({"response": generated_output})
