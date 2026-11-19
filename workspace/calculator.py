def add(a, b):
    return a + b  # Fixed: restored addition

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    print("=== Python Calculator ===")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter choice (1/2/3/4): ").strip()
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select a valid operation (1/2/3/4).")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    try:
        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'
        
        # Format output to remove trailing .0 if it's an integer
        if result.is_integer():
            result = int(result)
        
        if num1.is_integer():
            num1 = int(num1)
        if num2.is_integer():
            num2 = int(num2)
            
        print(f"Result: {num1} {op} {num2} = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
