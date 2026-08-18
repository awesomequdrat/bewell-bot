# This is for (SQLite database setup)

# This is going to import sqlite3

import sqlite3
# It connects to SQLite database and it creates chatbot.db if it doesn't exist already

# This is going to store all chatbot's data
conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()


# Here is the user table for account creation

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


# Mood check-in table (logs user moods)
cursor.execute("""
CREATE TABLE IF NOT EXISTS mood_checkins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    mood TEXT NOT NULL,
    sleep_quality TEXT,
    meals TEXT,
    exercise TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# Chat history table (logs user conversations with the bot)
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# Productivity & wellness reminders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    reminder_text TEXT NOT NULL,
    reminder_time TIMESTAMP,
    status TEXT DEFAULT 'pending',
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# Commit and close connection
# Commits (saves) all changes made to the database.
conn.commit()
# It closes the connection to the database.
conn.close()

print("Database and tables created successfully!")





