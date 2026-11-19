import unittest
from projects.student import calculate_grade

class TestStudentGrade(unittest.TestCase):
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(95), 'A')
        self.assertEqual(calculate_grade(90), 'A')
        self.assertEqual(calculate_grade(85), 'B')
        self.assertEqual(calculate_grade(80), 'B')
        self.assertEqual(calculate_grade(75), 'C')
        self.assertEqual(calculate_grade(70), 'C')
        self.assertEqual(calculate_grade(65), 'D')
        self.assertEqual(calculate_grade(60), 'D')
        self.assertEqual(calculate_grade(50), 'F')
        self.assertEqual(calculate_grade(0), 'F')

if __name__ == '__main__':
    unittest.main()
