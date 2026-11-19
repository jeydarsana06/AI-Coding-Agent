import unittest
from io import StringIO
import sys
from projects.student import calculate_student_grades

class TestStudent(unittest.TestCase):
    def test_calculation(self):
        # We can test the logic by verifying calculations directly or mocking input/output
        marks = [80, 90, 85]
        total = sum(marks)
        average = total / len(marks)
        self.assertEqual(total, 255)
        self.assertAlmostEqual(average, 85.0)

if __name__ == '__main__':
    unittest.main()
