import unittest
from pds.data_structure.recursion import fibonacci

class fibonacci_test(unittest.TestCase):
    def setUp(self):
        print("Test starting!")

    def tearDown(self):
        print("Test end!")

    def test_fib(self):
        self.assertEqual(fibonacci.fib(3), 2)


if __name__ == '__main__':
    unittest.main(verbosity=1)
