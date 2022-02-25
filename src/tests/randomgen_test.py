import unittest
from services.randomgen import RandomGen

class TestRandomgen(unittest.TestCase):

    def setUp(self) -> None:
        self.test_randomgen = RandomGen()
    
    def test_cant_pass_incorrect_arguments(self):
        self.assertIsNone(self.test_randomgen.random_number("a","b"))
        self.assertIsNone(self.test_randomgen.random_number(-1,-2))
        self.assertIsNone(self.test_randomgen.random_number(2,1))
        self.assertIsNone(self.test_randomgen.random_number(0,10**21))
    
    def test_can_pass_correct_arguments(self):
        self.assertIsNotNone(self.test_randomgen.random_number(1,3))

    def test_number_in_bounds(self):
        for i in range(100):
            self.assertEqual(1,self.test_randomgen.random_number(1,2))
            self.assertEqual(1001,self.test_randomgen.random_number(1001,1002))        

    def test_if_bounds_same(self):
        self.assertEqual(10,self.test_randomgen.random_number(10,10))
    
    def test_divider_resets(self):
        self.test_randomgen.divider= 9999999999999999999999999999999999 
        self.test_randomgen.random_number()
        self.assertEqual(1, self.test_randomgen.divider)