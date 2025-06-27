from flask import Flask, request, jsonify
from model import generate_reply
from filter import is_offensive
import json, csv, os
from datetime import datetime

app = Flask(__name__)

# Load fallback responses
with open("dialogue_fallbacks.json") as f:
    fallbacks = json.load(f)["fallbacks"]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    user_input_lower = user_input.lower()

    # Check for fallback keywords
    matched_fallback = None
    for keyword in fallbacks:
        if keyword in user_input_lower:
            matched_fallback = fallbacks[keyword]
            break

    if matched_fallback:
        bot_reply = matched_fallback
    elif is_offensive(user_input):
        bot_reply = "Let's try to keep things respectful. I'm here to support you."
    else:
        bot_reply, _ = generate_reply(user_input)

    save_log(user_input, bot_reply)
    return jsonify({"reply": bot_reply})

def save_log(user_input, bot_reply):
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/session_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "user_input", "bot_reply"])  # add header if new
        writer.writerow([datetime.now().isoformat(), user_input, bot_reply])

if __name__ == "__main__":
    app.run(debug=True)

