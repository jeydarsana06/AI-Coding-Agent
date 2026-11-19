import os
import ast
import subprocess
import sys

# Always locate workspace relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.realpath(os.path.join(BASE_DIR, "workspace"))

os.makedirs(WORKSPACE, exist_ok=True)


def get_safe_path(filename: str) -> str:
    """Ensure file operations stay inside the workspace."""

    filepath = os.path.realpath(os.path.join(WORKSPACE, filename))

    try:
        if os.path.commonpath([WORKSPACE, filepath]) != WORKSPACE:
            raise ValueError("Access outside workspace is not allowed.")
    except ValueError:
        raise ValueError("Invalid file path.")

    return filepath


def create_directory(dirname: str) -> str:
    """Create a directory inside the workspace."""

    try:
        dirpath = get_safe_path(dirname)
        os.makedirs(dirpath, exist_ok=True)
        return f"Directory '{dirname}' created successfully."
    except Exception as e:
        return f"Error creating directory: {e}"


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
    """Read an existing file."""

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
    """List files inside the workspace."""

    files = []

    for root, dirs, filenames in os.walk(WORKSPACE):
        dirs[:] = sorted(
            d for d in dirs if d != "__pycache__"
        )

        for filename in sorted(filenames):
            if filename.endswith(".pyc"):
                continue

            filepath = os.path.join(root, filename)

            files.append(
                os.path.relpath(filepath, WORKSPACE)
            )

    return files


def check_python_syntax(filename: str) -> str:
    """Check Python files for syntax errors."""

    try:
        filepath = get_safe_path(filename)

        if not os.path.isfile(filepath):
            return "Error: File does not exist."

        if not filename.lower().endswith(".py"):
            return "Error: Only Python files can be checked."

        with open(filepath, "r", encoding="utf-8") as file:
            source = file.read()

        ast.parse(source, filename=filename)

        return f"Syntax check passed for '{filename}'."

    except SyntaxError as e:
        return (
            f"Syntax error in '{filename}' "
            f"at line {e.lineno}: {e.msg}"
        )

    except Exception as e:
        return f"Syntax checking error: {e}"


def execute_python(filename: str) -> str:
    """Execute Python files with timeout and error capture."""

    try:
        filepath = get_safe_path(filename)

        if not os.path.isfile(filepath):
            return "Error: File does not exist."

        if not filename.lower().endswith(".py"):
            return "Error: Only Python files can be executed."

        # Check syntax before execution
        syntax_result = check_python_syntax(filename)

        if not syntax_result.startswith("Syntax check passed"):
            return syntax_result

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


def run_tests(test_directory: str = ".") -> str:
    """Discover and execute unittest test cases."""

    try:
        directory = get_safe_path(test_directory)

        if not os.path.isdir(directory):
            return "Error: Test directory does not exist."

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                directory,
                "-p",
                "test*.py"
            ],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=WORKSPACE
        )

        output = result.stdout + result.stderr

        if "Ran 0 tests" in output:
            return "No tests were discovered.\n" + output

        return (
            f"Test Exit Code: {result.returncode}\n"
            f"Test Results:\n{output}"
        )

    except subprocess.TimeoutExpired:
        return "Error: Tests timed out after 30 seconds."

    except Exception as e:
        return f"Test execution error: {e}"