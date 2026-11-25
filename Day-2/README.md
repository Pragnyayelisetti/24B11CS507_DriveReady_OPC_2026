# Day 2 - AI Chatbot with Conversation Memory

## Sweet Crumbs Home Bakery AI Assistant 🍰

### Objective
To develop an interactive AI chatbot for Sweet Crumbs Home Bakery using the Groq API with conversation memory and error handling.

### Concepts Learned
- System, user and assistant roles
- System prompts
- Few-shot prompting
- Python dictionaries and JSON
- Conversation memory
- Functions and type hints
- Decorators
- Exception handling

### Features Implemented
- Continuous customer interaction
- Remembers recent customer conversations
- Provides bakery menu and pricing information
- Calculates product prices
- Function logging using decorators
- Conversation history trimming
- Rate-limit and connection error handling
- English and Telugu language support

### Technologies Used
- Python
- Google Colab
- Groq API
- OpenAI SDK

### How to Run
1. Install the `openai` library.
2. Configure `GROK_API_KEY` in Colab Secrets.
3. Open and run `day2_bakery_chatbot.py` in Google Colab.
4. Enter customer questions.
5. Type `exit`, `bye`, or `quit` to terminate the chatbot.

> Keep your API key secret. Never upload it to GitHub.

### Example
- Ask the chatbot about cake prices.
- Calculate the price of 6 cupcakes.
- Continue a conversation and test its memory.

### Learning Outcome
Understanding how to build an interactive AI chatbot using system prompts, conversation memory, Python functions, decorators and exception handling.
