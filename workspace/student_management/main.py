#!/usr/bin/env python3
"""
Student Grade Management System
A robust command-line application to manage student records, marks, grades, and averages.
"""

import sys

# In-memory database of students
# Format: { student_id: { 'name': str, 'marks': { subject: mark } } }
students = {}

def validate_marks(marks):
    """
    Validate that marks are between 0 and 100 inclusive.
    Raises ValueError if invalid.
    """
    if not isinstance(marks, dict):
        raise TypeError("Marks must be a dictionary of subject: mark pairs.")
    validated = {}
    for subject, mark in marks.items():
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject name must be a non-empty string.")
        try:
            m = float(mark)
        except (ValueError, TypeError):
            raise ValueError(f"Mark for '{subject}' must be a numeric value.")
        if not (0.0 <= m <= 100.0):
            raise ValueError(f"Mark for '{subject}' must be between 0 and 100 (got {mark}).")
        validated[subject.strip()] = m
    return validated

def add_student(student_id, name, marks=None):
    """
    Add a student record.
    student_id: unique identifier (str or int)
    name: student full name (str)
    marks: optional dict of {subject: mark}
    """
    s_id = str(student_id).strip()
    if not s_id:
        raise ValueError("Student ID cannot be empty.")
    
    s_name = str(name).strip()
    if not s_name:
        raise ValueError("Student name cannot be empty.")
        
    if s_id in students:
        raise ValueError(f"Student ID '{s_id}' already exists.")
        
    validated_marks = {}
    if marks:
        validated_marks = validate_marks(marks)
        
    students[s_id] = {
        'name': s_name,
        'marks': validated_marks
    }
    return students[s_id]

def add_marks(student_id, marks):
    """
    Add or update marks for an existing student.
    """
    s_id = str(student_id).strip()
    if s_id not in students:
        raise ValueError(f"Student ID '{s_id}' not found.")
    
    validated_marks = validate_marks(marks)
    students[s_id]['marks'].update(validated_marks)
    return students[s_id]

def calculate_average(marks):
    """
    Calculate the average mark from a dictionary of marks.
    Handles empty records / empty marks gracefully (returns 0.0).
    """
    if not marks or not isinstance(marks, dict):
        return 0.0
    total = sum(marks.values())
    count = len(marks)
    return round(total / count, 2)

def calculate_grade(average):
    """
    Determine letter grade based on average mark:
    90 - 100: A
    80 - 89.99: B
    70 - 79.99: C
    60 - 69.99: D
    Below 60: F
    """
    try:
        avg = float(average)
    except (ValueError, TypeError):
        return 'F'
        
    if avg >= 90.0:
        return 'A'
    elif avg >= 80.0:
        return 'B'
    elif avg >= 70.0:
        return 'C'
    elif avg >= 60.0:
        return 'D'
    else:
        return 'F'

def get_student_summary(student_id):
    """
    Get summary for a specific student including average and grade.
    Handles empty student records.
    """
    s_id = str(student_id).strip()
    if s_id not in students:
        raise ValueError(f"Student ID '{s_id}' not found.")
        
    record = students[s_id]
    name = record['name']
    marks = record['marks']
    
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    
    return {
        'id': s_id,
        'name': name,
        'marks': marks,
        'average': avg,
        'grade': grade
    }

def get_all_students_summary():
    """
    Get summary for all student records. Handles empty records list.
    """
    summaries = []
    for s_id in students:
        summaries.append(get_student_summary(s_id))
    return summaries

def load_sample_data():
    """
    Include sample student records into the system.
    """
    samples = [
        {"id": "S101", "name": "Alice Smith", "marks": {"Math": 92.5, "English": 88.0, "Science": 95.0}},
        {"id": "S102", "name": "Bob Jones", "marks": {"Math": 74.0, "English": 65.5, "Science": 70.0}},
        {"id": "S103", "name": "Charlie Brown", "marks": {"Math": 55.0, "English": 60.0, "Science": 52.0}},
        {"id": "S104", "name": "Diana Prince", "marks": {}},  # Empty marks record test
        {"id": "S105", "name": "Evan Wright", "marks": {"Math": 85.0, "English": 90.0}}
    ]
    
    for sample in samples:
        s_id = sample["id"]
        if s_id not in students:
            add_student(s_id, sample["name"], sample["marks"])
    return students

def display_report():
    """
    Display formatted report of all student records.
    """
    print("\n" + "="*70)
    print(f"{'STUDENT GRADE MANAGEMENT SYSTEM REPORT':^70}")
    print("="*70)
    
    summaries = get_all_students_summary()
    if not summaries:
        print("\nNo student records found in the system.")
        print("="*70)
        return

    print(f"{'ID':<8} | {'Name':<18} | {'Subjects & Marks':<25} | {'Avg':<6} | {'Grade':<5}")
    print("-" * 70)
    
    for s in summaries:
        marks_str = ", ".join([f"{sub}: {m}" for sub, m in s['marks'].items()]) if s['marks'] else "No marks recorded"
        print(f"{s['id']:<8} | {s['name']:<18} | {marks_str:<25} | {s['average']:<6.2f} | {s['grade']:<5}")
    
    print("="*70)

def main():
    """
    Main entry point for interactive or automated execution.
    """
    print("Initializing Student Grade Management System...")
    load_sample_data()
    display_report()

    # Calculate overall class average if any students exist
    summaries = get_all_students_summary()
    if summaries:
        class_avg = sum(s['average'] for s in summaries) / len(summaries)
        print(f"\nOverall Class Average: {class_avg:.2f}")
    print("\nSystem execution completed successfully.\n")

if __name__ == "__main__":
    main()
