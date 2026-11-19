from google import genai
from google.genai import types, errors

from config import API_KEY
from tools import (
    create_file,
    read_file,
    list_files,
    edit_file,
    execute_python,
    create_directory,
    check_python_syntax,
    run_tests
)

import time


# ==========================================
# GEMINI CONFIGURATION
# ==========================================

MODEL_NAME = "gemini-3.5-flash-lite"

client = genai.Client(api_key=API_KEY)


# ==========================================
# SYSTEM INSTRUCTIONS
# ==========================================

SYSTEM_INSTRUCTION = """
You are an autonomous AI Coding Agent.

Your responsibility is to understand coding instructions,
plan tasks, execute tools, verify results, and report completion.

AVAILABLE TOOLS:

1. create_file
2. read_file
3. edit_file
4. list_files
5. create_directory
6. execute_python
7. check_python_syntax
8. run_tests

EXECUTION RULES:

1. Understand the user's request before acting.
2. Break complex tasks into smaller steps.
3. Use the appropriate tools to perform actual operations.
4. Never claim a file was created or modified without using tools.
5. Check Python syntax before executing Python programs.
6. Analyze execution errors and fix them when appropriate.
7. Read files when their contents need verification.
8. Run tests when requested.
9. Complete dependent steps in the correct order.
10. Stop when the task is completed or cannot safely continue.
11. Never invent tool execution results.
12. Clearly communicate the final outcome.

FILE MANAGEMENT:

- All file operations must remain inside the workspace.
- Use relative file paths.
- Do not overwrite existing files unless requested.
- Create directories when required.

CODE QUALITY:

- Generate readable and properly structured code.
- Handle common errors.
- Prefer simple and maintainable solutions.
- Verify generated code before reporting success.

You are expected to behave as an agent,
not merely as a question-answering chatbot.
"""


# ==========================================
# AVAILABLE TOOLS
# ==========================================

TOOLS = [
    create_file,
    read_file,
    list_files,
    edit_file,
    create_directory,
    execute_python,
    check_python_syntax,
    run_tests
]


# ==========================================
# CHAT SESSION
# ==========================================

chat = client.chats.create(
    model=MODEL_NAME,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        tools=TOOLS,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            maximum_remote_calls=15
        ),
        temperature=0.2
    )
)


# ==========================================
# AI AGENT EXECUTION
# ==========================================

def ask_llm(user_message):

    if not user_message or not user_message.strip():
        return "Please enter a valid instruction."

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = chat.send_message(user_message)

            if response.text:
                return response.text

            return "Task processed, but Gemini returned no text response."

        except errors.ServerError as e:

            print(f"Gemini server error: {e}")

            if attempt < max_retries - 1:

                wait_time = 2 ** attempt

                print(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:
                return (
                    "Gemini server is temporarily unavailable. "
                    "Please try again later."
                )

        except errors.APIError as e:

            return f"Gemini API error: {e}"

        except Exception as e:

            return f"Unexpected agent error: {e}"
