import os

WORKSPACE = "workspace"


def create_file(filename, content):
    """Create a file inside the workspace."""

    filepath = os.path.join(WORKSPACE, filename)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return f"File '{filename}' created successfully."


def read_file(filename):
    """Read the contents of a file."""

    filepath = os.path.join(WORKSPACE, filename)

    if not os.path.exists(filepath):
        return "Error: File does not exist."

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def list_files():
    """List all files inside the workspace."""

    files = []

    for root, dirs, filenames in os.walk(WORKSPACE):
        for filename in filenames:
            files.append(os.path.relpath(
                os.path.join(root, filename), WORKSPACE
            ))

    return files