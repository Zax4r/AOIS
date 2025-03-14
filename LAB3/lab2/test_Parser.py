import unittest
from .Parser import *
class test_Parser(unittest.TestCase):

    def test_arguments(self):
        test_str = "(a&b)|(c&d)"
        self.assertEqual(["a","b","c","d"], Parser.get_arguments(test_str))

    def test_work_w_str(self):
        s = "a&b"
        letters = ["a", "b"]
        generator = Parser.work_w_str(s, letters)
        results = list(generator)        
        self.assertEqual(results,[("0&0", [0, 0]),("0&1", [0, 1]),("1&0", [1, 0]),("1&1", [1, 1])])
        
    def test_brackets(self):
        test_str = "(0)"
        self.assertEqual("0", Parser.delete_brackets(test_str))