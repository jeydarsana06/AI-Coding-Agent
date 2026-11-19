def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    print("Testing calculator.py functions:")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"subtract(10, 5) = {subtract(10, 5)}")
    print(f"multiply(10, 5) = {multiply(10, 5)}")
    print(f"divide(10, 5) = {divide(10, 5)}")
    
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Caught expected error on division by zero: {e}")
