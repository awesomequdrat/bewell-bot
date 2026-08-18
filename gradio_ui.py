# This is for (Gradio chatbot UI) without Flask
import gradio as gr
import sqlite3
import openai
import os
from dotenv import load_dotenv  # Load environment variables

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if OpenAI API Key is set
if not openai.api_key:
    raise ValueError(" OpenAI API key is missing! Set it in a .env file.")

# Function to generate chatbot response using OpenAI API
def chatbot_ui(user_input, user_id=1):
    try:
        response = openai.Completion.create(
            model="gpt-3.5",  # Use "gpt-3.5-turbo" if needed
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

# Gradio UI Chatbot Interface
chat_interface = gr.Interface(
    fn=chatbot_ui,
    inputs="text",
    outputs="text",
    title="Axe Hacks - Wellness Chatbot",
    description="A mental wellness chatbot for mood tracking and productivity.",
    theme="default"
)

# Run Gradio app
if __name__ == "__main__":
    chat_interface.launch()
