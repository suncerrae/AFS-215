import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        for i in [2, 4, 6, 8]:
            print('testing', i)
            assert fizzbuzz(i) == 'Fizz'

    def test_buzz(self):
        for i in [5, 10, 50]:
            print('testing', i)
            assert fizzbuzz(i) == 'Buzz'

    def test_fizzbuzz(self):
        for i in [15, 30, 85]:
            print('testing', i)
            assert fizzbuzz(i) == 'FizzBuzz'