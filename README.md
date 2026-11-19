# AI Coding Agent

An AI-powered coding assistant built using Python and Google's Gemini API. It understands natural-language programming instructions and performs coding tasks through automated tool execution.

## Features

- Natural-language instruction processing.
- Automatic Python file creation and modification.
- Workspace file and directory management.
- Python code execution.
- Syntax error detection.
- Automated unit testing.
- Multi-step task execution.
- Error handling and execution timeouts.
- Student Grade Management System project generation.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- Python AST
- Subprocess
- Unittest
- Python-dotenv

## Project Structure

```text
AI-Coding-Agent/
│
├── main.py
├── agent.py
├── tools.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
│
└── workspace/
    ├── hello.py
    ├── multi_test/
    │   └── calculator.py
    │
    └── student_management/
        ├── main.py
        └── test_main.py
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Coding-Agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload your API key to GitHub.

### 6. Run the application

```bash
python main.py
```

## Example Instructions

The agent supports instructions such as:

- Create a Python file that prints Hello World.
- List all files in my workspace.
- Modify an existing Python file.
- Create a calculator with mathematical operations.
- Generate a complete Student Grade Management System.
- Check Python syntax and execute programs.
- Discover and run unit tests.

## Testing

Run unit tests using:

```bash
python -m unittest discover -s workspace/student_management -p "test*.py" -v
```

## Architecture

The application follows a tool-based AI agent architecture.

1. User provides a natural-language instruction.
2. Gemini processes the instruction.
3. Gemini selects appropriate tools.
4. Python tools execute the requested operations.
5. Execution results are returned to Gemini.
6. Gemini provides the final response.

## Security and Error Handling

- Workspace path validation.
- Prevention of file access outside the workspace.
- Python syntax validation.
- Execution timeout handling.
- Exception handling.
- API error handling.

## Future Enhancements

- Support for additional programming languages.
- Improved autonomous debugging.
- Git integration.
- Code optimization and review.
- Graphical user interface.

## Author

Developed as part of the AI Coding Agent project.