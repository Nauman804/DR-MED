from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
# ✅ Safe API key load
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment")

client = Groq(api_key=api_key)

# ── System Prompt ──
SYSTEM_PROMPT = """You are MediBot, a helpful health assistant dedicated to providing accurate, safe, and compassionate health information. You specialize in:

- Symptom analysis and guidance
- Medication information and dosages
- Wellness and preventive health tips
- Mental health support and resources
- Nutrition and diet recommendations
- First aid information

IMPORTANT RULES:
1. Always remind users to consult a doctor for serious concerns
2. Never provide definitive medical diagnoses
3. Be empathetic and supportive in your responses
4. If asked about suicidal thoughts or severe emergencies, provide crisis hotline numbers
5. Keep responses clear, concise, and easy to understand
6. Ask clarifying questions when needed

Start conversations warmly and end with helpful suggestions."""

@app.route("/")
def index():
    return send_from_directory('../public', 'index.html')


@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        # ✅ SAFE JSON handling (IMPORTANT FIX)
        data = request.get_json(silent=True) or {}

        user_message = data.get("message", "").strip()
        history = data.get("history", [])

        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        # Build messages
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for h in history[-10:]:
            messages.append({
                "role": h.get("role", "user"),
                "content": h.get("content", "")
            })

        messages.append({"role": "user", "content": user_message})

        # AI call
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            max_tokens=512,
            temperature=0.6,
        )

        reply = response.choices[0].message.content.strip()

        return jsonify({
            "reply": reply,
            "safe_flag": False
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

# Vercel ke liye
app = app  # Export for Vercel