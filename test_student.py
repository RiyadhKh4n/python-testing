import unittest
from student import Student

class TestStudents(unittest.TestCase):
    
    def test_full_name(self):
        student = Student('John', 'Doe')
        self.assertEqual(student.full_name, 'John Doe')

    def test_naughty_list(self):
        student = Student('John', 'Doe')
        student.test_naughty_list()

        self.assertTrue(student.naughty_list, True)

    def test_email(self):
        student = Student("John",  "Doe")
        self.assertEqual(student.email, "john.doe@email.com")


if __name__ == '__main__':
    unittest.main()