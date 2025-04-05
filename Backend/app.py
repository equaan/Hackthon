# backend/app.py

from flask import Flask, request, jsonify
from bedrock_client import generate_study_routine

app = Flask(__name__)

@app.route("/generate-routine", methods=["POST"])
def generate_routine():
   """
    Accepts a JSON payload with a 'user_input' field and returns a study routine along with a motivational quote.
    """
    data = request.get_json()
    user_input = data.get("user_input", "")
    routine = generate_study_routine(user_input)
    return jsonify({"routine": routine}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

