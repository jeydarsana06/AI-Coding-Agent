from tools import create_file, read_file, list_files

# Create a file
print(create_file("hello.py", "print('Hello, World!')"))

# Read the file
print(read_file("hello.py"))

# List workspace files
print(list_files())