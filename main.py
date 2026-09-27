import os

from dotenv import load_dotenv
from openai import OpenAI
import openai


# ============================================
# 1. Load environment variables
# ============================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


# ============================================
# 2. Validate API key
# ============================================

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing from .env"
    )


# ============================================
# 3. Create OpenAI client
# ============================================

client = OpenAI(
    api_key=api_key
)


# ============================================
# 4. System prompt
# ============================================

SYSTEM_PROMPT = """
You are a helpful AI assistant running in the terminal.

Give clear, accurate, and beginner-friendly answers.

When explaining technical concepts:
- Use simple language.
- Give practical examples.
- Avoid unnecessary complexity.
"""


# ============================================
# 5. Model
# ============================================

MODEL_NAME = "gpt-5.5"


# ============================================
# 6. Call OpenAI
# ============================================

def call_ai(messages):

    try:

        response = client.responses.create(
            model=MODEL_NAME,
            instructions=SYSTEM_PROMPT,
            input=messages
        )

        return response

    except openai.AuthenticationError:

        print(
            "\nAuthentication error."
            "\nPlease check your OPENAI_API_KEY.\n"
        )

        return None

    except openai.RateLimitError:

        print(
            "\nRate limit or quota exceeded."
            "\nPlease wait and try again later.\n"
        )

        return None

    except openai.APIConnectionError:

        print(
            "\nConnection error."
            "\nPlease check your internet connection "
            "and try again.\n"
        )

        return None

    except openai.APIStatusError as error:

        print(
            f"\nOpenAI API error "
            f"({error.status_code}): {error.message}\n"
        )

        return None

    except openai.APIError as error:

        print(
            f"\nOpenAI API error: {error}\n"
        )

        return None

    except Exception as error:

        print(
            f"\nUnexpected error: {error}\n"
        )

        return None


# ============================================
# 7. Display AI response
# ============================================

def display_response(response):

    # ----------------------------------------
    # Answer
    # ----------------------------------------

    print(
        f"\nAssistant: {response.output_text}"
    )

    # ----------------------------------------
    # Model
    # ----------------------------------------

    print(
        f"\nModel: {response.model}"
    )

    # ----------------------------------------
    # Token usage
    # ----------------------------------------

    if response.usage:

        print("\nToken usage:")

        print(
            f"  Input:  {response.usage.input_tokens}"
        )

        print(
            f"  Output: {response.usage.output_tokens}"
        )

        print(
            f"  Total:  {response.usage.total_tokens}"
        )

    else:

        print(
            "\nToken usage: Not available"
        )

    print()


# ============================================
# 8. Help command
# ============================================

def show_help():

    print("""
Available commands:

help  - Show available commands
clear - Clear conversation history
quit  - Exit the assistant
""")


# ============================================
# 9. Conversation history
# ============================================

conversation = []


# ============================================
# 10. Startup message
# ============================================

print("=" * 45)
print("          Terminal AI Assistant")
print("=" * 45)
print()

print(f"Model: {MODEL_NAME}")
print()

print("Type 'help' to see available commands.")
print("Type 'clear' to clear the conversation.")
print("Type 'quit' to exit.")
print()


# ============================================
# 11. Main loop
# ============================================

while True:

    try:

        user_input = input("You: ").strip()

    except KeyboardInterrupt:

        print("\n\nGoodbye!")

        break

    except EOFError:

        print("\n\nGoodbye!")

        break

    # ----------------------------------------
    # Ignore empty input
    # ----------------------------------------

    if not user_input:
        continue

    # ----------------------------------------
    # Quit
    # ----------------------------------------

    if user_input.lower() == "quit":

        print("\nGoodbye!")

        break

    # ----------------------------------------
    # Help
    # ----------------------------------------

    if user_input.lower() == "help":

        show_help()

        continue

    # ----------------------------------------
    # Clear conversation
    # ----------------------------------------

    if user_input.lower() == "clear":

        conversation.clear()

        print("\nConversation cleared.\n")

        continue

    # ----------------------------------------
    # Add user message
    # ----------------------------------------

    conversation.append({
        "role": "user",
        "content": user_input
    })

    # ----------------------------------------
    # Call OpenAI
    # ----------------------------------------

    response = call_ai(conversation)

    # ----------------------------------------
    # API request failed
    # ----------------------------------------

    if response is None:

        # Remove the user message because
        # it was not successfully processed.

        conversation.pop()

        continue

    # ----------------------------------------
    # Display response
    # ----------------------------------------

    display_response(response)

    # ----------------------------------------
    # Add assistant response to history
    # ----------------------------------------

    conversation.append({
        "role": "assistant",
        "content": response.output_text
    })
