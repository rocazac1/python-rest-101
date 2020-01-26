import unittest
from models import Person

class TestPerson(unittest.TestCase):
    def test_str(self):
        actual = Person("Robert", 27).__str__()
        self.assertEqual('name = Robert, age = 27', actual)
    def test_isAdult(self):
        actual = Person("Robert", 27).isAdult()
        self.assertEqual(True, actual)
    def test_isNotAdult(self):
        actual = Person("Charlotte", 1).isAdult()
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()
