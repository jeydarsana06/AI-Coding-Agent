from tools import create_file, read_file, list_files

# Test 1: Create a file
print("\n--- Testing File Creation ---")
result = create_file("hello.py", "print('Hello from AI Coding Agent!')")
print(result)

# Test 2: Read the file
print("\n--- Testing File Reading ---")
content = read_file("hello.py")
print(content)

# Test 3: List files
print("\n--- Testing File Listing ---")
files = list_files()
print(files)