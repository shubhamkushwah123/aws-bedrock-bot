from flask import Flask, request, render_template, jsonify
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
BEDROCK_API_URL = "https://bedrock-runtime.us-east-1.amazonaws.com/model/meta.llama3-8b-instruct-v1:0/invoke"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('AWS_BEARER_TOKEN_BEDROCK')}",
    "Content-Type": "application/json",
    "X-Amz-Bedrock-Invocation-Type": "POST"
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("prompt")
        response_text = call_bedrock_model(user_input)
        return render_template("index.html", user_input=user_input, response_text=response_text)
    return render_template("index.html")

def call_bedrock_model(prompt):
    formatted_prompt = f"User: {prompt}\nAssistant:"
    body = {
        "prompt": formatted_prompt,
        "max_gen_len": 300,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        response = httpx.post(
            BEDROCK_API_URL,
            headers=HEADERS,
            json=body,
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data["generation"] if "generation" in data else "No output returned."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
