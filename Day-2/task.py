# Day 2 — Sweet Crumbs Home Bakery AI Chatbot with Memory
# Run in Google Colab. Add your Groq API key in Colab Secrets as GROK_API_KEY.

!pip install -q openai

import json
import functools
from google.colab import userdata
from openai import OpenAI, RateLimitError, APIConnectionError

# Connect to Groq
client = OpenAI(
    api_key=userdata.get("GROK_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"

# Bakery menu
MENU = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80
}

# Instructions for the chatbot
SYSTEM = f"""
ROLE: You are the friendly assistant for Sweet Crumbs Home Bakery.

FACTS: Menu with prices in rupees: {json.dumps(MENU)}
Orders need 24 hours' notice.
All cakes have eggless versions.

RULES: Never promise a delivery time.
If it isn't in FACTS, say "I'll check with the owner."
Remember the customer's name and order during the chat.

FORMAT: Under 50 words, friendly,
English or Telugu matching the customer.
"""

# Decorator for logging function calls
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[log] {func.__name__}{args} -> {result!r}")
        return result
    return wrapper

# Calculate price for an item and quantity
@log_call
def get_price(item: str, qty: int = 1) -> int:
    """Return the total price for the given quantity."""
    return MENU[item.lower().strip()] * qty

# Store conversation history
history = [{"role": "system", "content": SYSTEM}]
MAX_TURNS = 8

# Send a message and get the chatbot response
def chat(user_text: str) -> str:
    history.append({
        "role": "user",
        "content": user_text
    })

    recent = [history[0]] + history[1:][-MAX_TURNS:]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent,
            temperature=0.3
        )

        reply = response.choices[0].message.content

    except RateLimitError:
        reply = "We're a little busy. Please try again."

    except APIConnectionError:
        reply = "I can't reach the server right now."

    history.append({
        "role": "assistant",
        "content": reply
    })

    return reply

# Start the chatbot
print("Welcome to Sweet Crumbs Home Bakery!")
print("Total for 6 cupcakes:", get_price("cupcake", 6))
print("Type exit to stop chatting.")

while True:
    text = input("You: ")

    if text.lower().strip() in ("bye", "exit", "quit"):
        print("Bot: Thank you for visiting Sweet Crumbs!")
        break

    print("Bot:", chat(text))
