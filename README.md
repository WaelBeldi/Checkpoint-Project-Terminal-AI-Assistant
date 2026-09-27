# Terminal AI Assistant

A simple terminal-based AI assistant built with Python and the OpenAI API.

This project introduces the fundamentals of working with an LLM API from Python without using an AI framework such as LangChain.

## Features

* OpenAI API integration
* System prompt
* Conversation history
* `help` command
* `clear` command
* `quit` command
* Model information
* Token usage information
* API error handling
* Environment variable configuration

## Project Structure

```text
terminal-ai-assistant/
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
└── docs/
```

### File Responsibilities

* `.env` — stores the local OpenAI API key
* `.env.example` — example environment configuration
* `.gitignore` — prevents secrets and generated files from being committed
* `main.py` — contains the assistant logic
* `requirements.txt` — lists Python dependencies
* `README.md` — project documentation

---

# Requirements

You need:

* Python 3.10+
* An OpenAI API key
* Internet connection

---

# 1. Create a Virtual Environment

From the project directory:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

After activation, your terminal should show:

```text
(venv)
```

---

# 2. Install Dependencies

Install the required packages:

```bash
pip install openai python-dotenv
```

Or, if `requirements.txt` already exists:

```bash
pip install -r requirements.txt
```

To generate or update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

# 3. Configure the API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the value with your actual OpenAI API key.

Do not commit `.env` to GitHub.

---

# 4. Run the Application

Start the assistant with:

```bash
python main.py
```

You should see:

```text
=============================================
          Terminal AI Assistant
=============================================

Model: gpt-5.5

Type 'help' to see available commands.
Type 'clear' to clear the conversation.
Type 'quit' to exit.

You:
```

---

# Available Commands

## `help`

Displays the available commands:

```text
help  - Show available commands
clear - Clear conversation history
quit  - Exit the assistant
```

## `clear`

Clears the current conversation history.

The next question starts a new conversation.

## `quit`

Exits the application.

You can also press `Ctrl+C` to exit.

---

# Example Interaction

```text
You: What is an API?

Assistant: An API is a way for different software applications
to communicate with each other. For example, a frontend
application can use an API to communicate with a backend server.

Model: gpt-5.5

Token usage:
  Input:  24
  Output: 45
  Total:  69

You: Give me another example.

Assistant: Sure. A weather application can use an API to request
weather information from a server. The server returns data such
as the temperature, humidity, and weather conditions.

Model: gpt-5.5

Token usage:
  Input:  82
  Output: 47
  Total:  129

You: clear

Conversation cleared.

You: quit

Goodbye!
```

The exact response and token counts will vary.

---

# Conversation History

The assistant stores the conversation in a Python list while the application is running.

For example:

```python
conversation = []
```

When the user sends a message, it is added:

```python
conversation.append({
    "role": "user",
    "content": user_input
})
```

After the AI responds, the assistant's response is also added:

```python
conversation.append({
    "role": "assistant",
    "content": response.output_text
})
```

The conversation therefore becomes:

```text
system instruction
       ↓
user
       ↓
assistant
       ↓
user
       ↓
assistant
       ↓
...
```

This allows the assistant to understand follow-up questions.

For example:

```text
You: What is an API?

Assistant: An API allows applications to communicate...

You: Give me another example.
```

Because the previous messages are included in the next API request, the model understands that "another example" refers to APIs.