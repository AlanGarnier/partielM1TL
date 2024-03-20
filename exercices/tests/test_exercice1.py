import unittest


# Function
def add(x, y):
    return x + y


# Test case pour tester la fonction add
class MyTestCase(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(10, 15), 25)

    def test_add_negative_number(self):
        self.assertEqual(add(-2, -2), -4)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
