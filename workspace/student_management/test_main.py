#!/usr/bin/env python3
"""
Unit tests for Student Grade Management System
Tests grade calculation, average marks calculation, validation, and empty record handling.
"""

import unittest
import sys
import os

# Ensure parent directory or current directory is in path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main import (
    students,
    validate_marks,
    add_student,
    add_marks,
    calculate_average,
    calculate_grade,
    get_student_summary,
    load_sample_data
)

class TestStudentGradeManagement(unittest.TestCase):
    
    def setUp(self):
        """Reset students dict before each test."""
        students.clear()

    def test_calculate_average_valid(self):
        """Test average calculation with valid marks."""
        marks = {"Math": 80.0, "English": 90.0, "Science": 100.0}
        avg = calculate_average(marks)
        self.assertEqual(avg, 90.0)

    def test_calculate_average_empty(self):
        """Test average calculation with empty or missing marks."""
        self.assertEqual(calculate_average({}), 0.0)
        self.assertEqual(calculate_average(None), 0.0)

    def test_calculate_average_rounding(self):
        """Test average calculation rounds correctly to 2 decimal places."""
        marks = {"Math": 85.0, "English": 86.0, "Science": 87.0}
        avg = calculate_average(marks)
        self.assertEqual(avg, 86.0)
        
        marks2 = {"Math": 33.33, "English": 33.34}
        self.assertEqual(calculate_average(marks2), 33.34)

    def test_calculate_grade_boundaries(self):
        """Test letter grade assignment based on averages."""
        self.assertEqual(calculate_grade(95.0), 'A')
        self.assertEqual(calculate_grade(90.0), 'A')
        self.assertEqual(calculate_grade(89.99), 'B')
        self.assertEqual(calculate_grade(80.0), 'B')
        self.assertEqual(calculate_grade(79.99), 'C')
        self.assertEqual(calculate_grade(70.0), 'C')
        self.assertEqual(calculate_grade(69.99), 'D')
        self.assertEqual(calculate_grade(60.0), 'D')
        self.assertEqual(calculate_grade(59.99), 'F')
        self.assertEqual(calculate_grade(0.0), 'F')

    def test_calculate_grade_invalid_input(self):
        """Test grade calculation handles invalid inputs gracefully."""
        self.assertEqual(calculate_grade("not-a-number"), 'F')
        self.assertEqual(calculate_grade(None), 'F')

    def test_validate_marks_valid(self):
        """Test mark validation accepts numbers between 0 and 100."""
        marks = {"Math": 0, "Science": 50, "English": 100.0, "History": "75"}
        validated = validate_marks(marks)
        self.assertEqual(validated["Math"], 0.0)
        self.assertEqual(validated["English"], 100.0)
        self.assertEqual(validated["History"], 75.0)

    def test_validate_marks_out_of_range(self):
        """Test mark validation rejects marks below 0 or above 100."""
        with self.assertRaises(ValueError):
            validate_marks({"Math": -0.1})
        with self.assertRaises(ValueError):
            validate_marks({"Math": 100.1})

    def test_validate_marks_invalid_type(self):
        """Test mark validation rejects non-numeric marks."""
        with self.assertRaises(ValueError):
            validate_marks({"Math": "abc"})
        with self.assertRaises(TypeError):
            validate_marks("not-a-dict")

    def test_add_student_success(self):
        """Test adding a valid student record."""
        student = add_student("S001", "Jane Doe", {"Math": 88.0})
        self.assertEqual(student['name'], "Jane Doe")
        self.assertEqual(student['marks']["Math"], 88.0)
        self.assertIn("S001", students)

    def test_add_student_empty_fields(self):
        """Test adding student with empty ID or name raises ValueError."""
        with self.assertRaises(ValueError):
            add_student("", "Jane Doe")
        with self.assertRaises(ValueError):
            add_student("S001", "")

    def test_add_student_duplicate_id(self):
        """Test adding duplicate student ID raises ValueError."""
        add_student("S001", "Jane Doe")
        with self.assertRaises(ValueError):
            add_student("S001", "John Smith")

    def test_handle_empty_student_records(self):
        """Test system behavior when student records or marks are empty."""
        # Add student with no marks
        add_student("S999", "Empty Marks Student", {})
        summary = get_student_summary("S999")
        self.assertEqual(summary['marks'], {})
        self.assertEqual(summary['average'], 0.0)
        self.assertEqual(summary['grade'], 'F')

    def test_load_sample_data(self):
        """Test loading sample student records."""
        load_sample_data()
        self.assertGreaterEqual(len(students), 5)
        # Check one sample student specifically
        self.assertIn("S101", students)
        self.assertEqual(students["S101"]["name"], "Alice Smith")


if __name__ == "__main__":
    unittest.main()
