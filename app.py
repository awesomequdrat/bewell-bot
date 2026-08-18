# This is for (Flask API backend)
from flask import Flask, request, jsonify
import sqlite3
import openai
import os
from dotenv import load_dotenv  # Load environment variables from .env file

"""
This will allow chatbot to:
- Process user messages.
- Store chat history in chatbot.db.
- Connect to OpenAI’s GPT API to generate chatbot responses.
- Send responses back to the user.
"""

# Load environment variables from .env
load_dotenv()

#  Initialize Flask app
app = Flask(__name__)

# Set OpenAI API Key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if OpenAI API Key is set
if not openai.api_key:
    raise ValueError(" OpenAI API key is missing! Set it in a .env file.")

# Function to generate chatbot response using OpenAI API
def chatbot_response(user_id, user_input):
    try:
        response = openai.Completion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a wellness chatbot helping users with mood tracking and productivity."},
                {"role": "user", "content": user_input}
            ]
        )
        
        bot_message = response.choices[0].message.content  # Corrected syntax

        # Store chat in database
        store_chat(user_id, user_input, bot_message)

        return bot_message

    except Exception as e:
        return f" Error generating response: {str(e)}"

# Store chat messages in the database
def store_chat(user_id, user_message, bot_response):
    try:
        conn = sqlite3.connect("chatbot.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO chat_history (user_id, user_message, bot_response) 
            VALUES (?, ?, ?)
        """, (user_id, user_message, bot_response))
        conn.commit()
    except Exception as e:
        print(f" Database error: {str(e)}")
    finally:
        conn.close()  # Ensures the connection is always closed

# API Route for Chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Missing message"}), 400
    
    user_id = data.get("user_id", 1)  # Default user_id = 1
    user_input = data["message"]
    
    response = chatbot_response(user_id, user_input)
    return jsonify({"response": response})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
