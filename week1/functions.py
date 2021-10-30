import unittest

class Test_PerfectNumber(unittest.TestCase):

    def perfect_number(self):
        sum = 0
        for x in range(1, self):
            if self % x == 0:
                sum += x
        return sum == self

    print(perfect_number(6))

if __name__ == '__main__':
    unittest.main()