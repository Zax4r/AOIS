import unittest
from .Operands import *
class test_Operands(unittest.TestCase):

    def test_unary(self):
        test_str = "!!!0"
        self.assertEqual("1", Operands.unary_operations(test_str))

    def test_binary_and(self):
        s = "0&1"
        self.assertEqual(Operands.calculate_primitives(s),"0")
    
    def test_binary_or(self):
        s = "0|1"
        self.assertEqual(Operands.calculate_primitives(s),"1")
    
    def test_binary_implication(self):
        s = "0>1"
        self.assertEqual(Operands.calculate_primitives(s),"1")

    def test_binary_equal(self):
        s = "0~1"
        self.assertEqual(Operands.calculate_primitives(s),"0")