# Day 1 — Sweet Crumbs Home Bakery AI Assistant
# Run in Google Colab. Add your Groq API key to Colab Secrets as GROQ_API_KEY.

!pip install -q openai

from google.colab import userdata
from openai import OpenAI

# Connect to Groq using the OpenAI-compatible client
client = OpenAI(
    api_key=userdata.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Bakery information and rules for the assistant
system_prompt = """
You are a friendly AI assistant for Sweet Crumbs Home Bakery.

Bakery facts:
- Cakes are baked to order.
- Customers should place orders at least 24 hours in advance.
- All cakes can be made in eggless versions.
- Plum cake: Rs 500
- Chocolate cake: Rs 650
- Cupcake: Rs 80

Rules:
- Never promise a delivery time.
- If you do not know an answer, say: "I'll check with the owner."
- Keep every answer within 50 words.
- Be friendly and respond in the customer's language when possible.
"""

# Ask the assistant a question
question = "Can I get an eggless cake today evening?"

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ],
    temperature=0.2
)

# Display the answer
print("Assistant:", response.choices[0].message.content)

# Display token usage
print("\nToken usage:")
print("Prompt tokens:", response.usage.prompt_tokens)
print("Completion tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)
