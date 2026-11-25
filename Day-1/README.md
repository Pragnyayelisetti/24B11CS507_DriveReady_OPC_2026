# Day 1 — LLM Basics & API Integration

## Sweet Crumbs Home Bakery AI Assistant 🍰

### Goal

Build a simple AI assistant for Sweet Crumbs Home Bakery using the Groq API. The assistant answers customer questions using bakery information and rules.

### What I learned

- **LLM (Large Language Model):** AI that generates text based on patterns learned from large amounts of data.
- **Next-token prediction:** The model generates text by predicting what token is likely to come next.
- **Tokens:** Small chunks of text processed by a model. API usage is often measured in tokens.
- **Temperature:** Controls how random or predictable the model's responses are. A low value gives more consistent responses.
- **Context window:** The amount of text a model can consider during one interaction.
- **Hallucination:** When an AI generates information that sounds plausible but is incorrect.
- **API integration:** Connecting our program to an AI service and sending it a request.

### Assistant features

- Answers bakery customer questions.
- Uses the menu and rules included in its system prompt.
- Keeps answers short and friendly.
- Responds in the customer's language when possible.
- Displays token usage after the request.

### Tech stack

- Python
- Google Colab
- Groq API
- OpenAI Python SDK (compatible API client)

### Run it

1. Open the Python file `day1_bakery_assistant.py` or copy its code into a Google Colab notebook.
2. Get a Groq API key from the Groq console.
3. In Google Colab, add the key in **Secrets** with the name `GROQ_API_KEY`.
4. Install the required package: `pip install openai`.
5. Run the code and ask the assistant a bakery-related question.

> **Keep your API key secret.** Never paste it into public code, screenshots, or GitHub.

### Example question

`Can I get an eggless cake today evening?`

### Day 1 outcome

I connected a Python program to an LLM API, configured the assistant with bakery-specific instructions, received a response, and inspected token usage.
