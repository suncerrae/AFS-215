import unittest

class Test_Fizz_Buzz(unittest.TestCase):
    def test_Fizz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')
       
       
    def test_Buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        

    def test_FizzBuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')
        


def fizzbuzz(a):
            if a % 3 == 0 and a % 5 == 0:
                return'fizzbuzz'
               
            elif a % 5 == 0:
                return 'buzz'
               
            elif a % 3 == 0:
                return 'fizz'
                
            else:
                return a

if __name__ == '__main__':
    unittest.main()