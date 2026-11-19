import os

def calculate_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average <= 89.99: # or check 80 <= average < 90
        return 'B'
    elif 70 <= average <= 79.99:
        return 'C'
    elif 60 <= average <= 69.99:
        return 'D'
    else:
        return 'F'

def calculate_student_grades():
    print("=== Student Grade Calculator ===")
    name = input("Enter student's name: ").strip()
    
    marks = []
    subjects = ["First", "Second", "Third"]
    
    for i in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks for {subjects[i]} subject (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    
    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total:.2f}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    calculate_student_grades()
