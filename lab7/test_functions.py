from functions import *
import unittest

class test_functions(unittest.TestCase):

    def test_functions(self):
        a=[0,0,0]
        b=[0,0,1]
        self.assertEqual(f2(a,b),[0,0,0])
        self.assertEqual(f7(a,b),[0,0,1])
        self.assertEqual(f8(a,b),[1,1,0])
        self.assertEqual(f13(a,b),[1,1,1])
        self.assertEqual(convert(a),0)