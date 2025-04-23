import random

from flask import Flask, jsonify, request

from src.generate import recommend_character

app = Flask(__name__)


# Canary rollout: 10% traffic to prod prompt, rest to staging
def select_prompt():
    if random.random() < 0.1:
        return "prompts/recommend.txt.prod"
    return "prompts/recommend.txt"


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    prompt_path = select_prompt()
    result = recommend_character(data["preferences"], prompt_path)
    return jsonify(result)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
