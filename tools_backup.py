import os
import subprocess
import sys

WORKSPACE = os.path.abspath("workspace")
os.makedirs(WORKSPACE, exist_ok=True)


def get_safe_path(filename: str) -> str:
    """Ensure file operations stay inside the workspace."""

    filepath = os.path.abspath(os.path.join(WORKSPACE, filename))

    if os.path.commonpath([WORKSPACE, filepath]) != WORKSPACE:
        raise ValueError("Access outside workspace is not allowed.")

    return filepath


def create_file(filename: str, content: str) -> str:
    """Create a new file inside the workspace."""

    try:
        filepath = get_safe_path(filename)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

        return f"File '{filename}' created successfully."

    except Exception as e:
        return f"Error creating file: {e}"


def read_file(filename: str) -> str:
    """Read the contents of an existing file."""

    try:
        filepath = get_safe_path(filename)

        if not os.path.isfile(filepath):
            return "Error: File does not exist."

        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        return f"Error reading file: {e}"


def edit_file(filename: str, content: str) -> str:
    """Modify an existing file."""

    try:
        filepath = get_safe_path(filename)

        if not os.path.isfile(filepath):
            return "Error: File does not exist."

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

        return f"File '{filename}' updated successfully."

    except Exception as e:
        return f"Error editing file: {e}"


def list_files() -> list[str]:
    """List all files inside the workspace."""

    files = []

    for root, dirs, filenames in os.walk(WORKSPACE):

        for filename in filenames:

            files.append(
                os.path.relpath(
                    os.path.join(root, filename),
                    WORKSPACE
                )
            )

    return files


def execute_python(filename: str) -> str:
    """Execute a Python file and capture its output."""

    try:
        filepath = get_safe_path(filename)

        if not os.path.isfile(filepath):
            return "Error: File does not exist."

        if not filename.endswith(".py"):
            return "Error: Only Python files can be executed."

        result = subprocess.run(
            [sys.executable, filepath],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=WORKSPACE
        )

        return (
            f"Exit Code: {result.returncode}\n"
            f"Output:\n{result.stdout}\n"
            f"Errors:\n{result.stderr}"
        )

    except subprocess.TimeoutExpired:
        return "Error: Execution timed out after 10 seconds."

    except Exception as e:
        return f"Execution error: {e}"
