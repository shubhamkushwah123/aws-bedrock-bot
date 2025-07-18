# 🧠 Bedrock Chat App using Flask + Meta LLaMA 3

This is a simple Flask web application that connects to **Amazon Bedrock** and allows users to chat with the **Meta LLaMA 3** model (`meta.llama3-70b-instruct-v1:0`) using a short-term bearer token.

---

## 🚀 Features

- Built with **Python Flask**
- Uses **Amazon Bedrock** to interact with LLaMA 3 via REST API
- Simple web UI to send and receive messages
- Supports short-term bearer token auth
- Easily extendable to support other models (Claude, Titan, Mistral)

---

## 🛠️ Tech Stack

- Python 3.8+
- Flask
- `httpx` for HTTP requests
- `.env` for managing secrets
- HTML + basic CSS for UI

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/bedrock-chat-app.git
cd bedrock-chat-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file with your short-term Bedrock bearer token:

```
AWS_BEARER_TOKEN_BEDROCK=your-bedrock-bearer-token-here
```

> ⚠️ This token must have access to `meta.llama3-70b-instruct-v1:0` and be valid for the region you're using (default is `us-east-1`).

---

## 🧪 Running the App

```bash
flask run
```

Visit: `http://127.0.0.1:5000` in your browser.

---

## 💬 Sample Prompt

Try something like:

> "Compare Python and JavaScript for web development."

The model will respond using LLaMA 3's instruction-tuned capabilities.

---

## 🌐 Switching to Other Models

To use a different model, update:

- `BEDROCK_API_URL` in `app.py`
- Payload structure in `call_bedrock_model()` based on that model’s expected format (e.g. Claude or Titan)

---

## 📁 Project Structure

```
.
├── app.py
├── .env
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## ✨ Credits

Created by [Shubham Singh Kushwah](https://github.com/yourusername)  
Built for developers experimenting with Generative AI via AWS Bedrock.