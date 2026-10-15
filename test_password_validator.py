import unittest
from password_validator import password_checker

class Test_password_valdiator(unittest.TestCase):

    def test_passwordIsNone(self):
        self.assertIsNone(password_checker(None))

    def test_password_isString(self):
        self.assertIsInstance(password_checker("kgomotso"), str)

    # def test_password_isAtleast_8chars(self):
    #     pass














if __name__ == "__main__":
    unittest.main()