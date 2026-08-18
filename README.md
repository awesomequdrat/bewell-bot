# BeWell Bot

**BeWell Bot** is a mental-wellness chatbot prototype created for **Axe Hacks** in March 2025. The project was recognized with a **3rd Place Golden Hack Award**.

The goal was to create a low-friction, judgment-free wellness companion for college students and working professionals who may only have a few minutes for a check-in, grounding exercise, reflection, or productivity reset.

## What it does

The prototype combines a conversational AI backend with a lightweight web interface and local persistence.

- Accepts text-based wellness conversations through a Gradio interface
- Exposes a Flask `/chat` API endpoint
- Uses the OpenAI API to generate conversational responses
- Stores chat history in SQLite
- Includes database tables designed for users, mood check-ins, chat history, and reminders
- Keeps the OpenAI API key outside the repository through environment variables

## Original product vision

The hackathon concept included:

- Quick mood check-ins
- Short grounding and mindfulness exercises
- Gratitude and journaling prompts
- Productivity reminders
- Guidance toward external wellness resources
- Future speech-to-text and audio responses
- Future calendar/reminder integrations

Some of these items were part of the product roadmap rather than completed features in the submitted prototype.

## Tech stack

- Python
- Flask
- Gradio
- SQLite
- OpenAI API
- python-dotenv

## Project structure

```text
bewell-bot/
├── app.py
├── database.py
├── gradio_ui.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the OpenAI API key

Copy `.env.example` to `.env` and add your own API key:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.6
```

Never commit your real `.env` file or API key.

### 4. Initialize the database

```bash
python database.py
```

### 5. Run the Gradio interface

```bash
python gradio_ui.py
```

Or run the Flask API:

```bash
python app.py
```

The Flask endpoint accepts a POST request at `/chat` with JSON like:

```json
{
  "user_id": 1,
  "message": "I feel stressed about everything I need to do today."
}
```

## Award

**3rd Place — Golden Hack Award, Axe Hacks (March 2025)**

## Safety and privacy

BeWell Bot is a hackathon prototype and is **not a medical device, therapist, crisis service, or substitute for professional mental-health care**.

The current prototype stores conversation text in a local SQLite database. Do not use it to collect real sensitive health information without implementing appropriate privacy, security, consent, retention, and access controls.

## Development note

The original hackathon code used an older OpenAI SDK calling style. This public-ready version updates the API calls to the current OpenAI Python client while preserving the prototype's core architecture.

## Credits

Built as a team project at Axe Hacks. Add the names and GitHub profiles of all contributors here before publishing the repository publicly.
