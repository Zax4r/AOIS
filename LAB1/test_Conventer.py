import unittest
from Converter import Converter

class Converter_to_B_Test(unittest.TestCase):
    def setUp(self):
        self.conv = Converter(8)
    
    def test_forward(self):
        self.assertEqual(self.conv.D_to_B_forward(73),[0, 1, 0, 0, 1, 0, 0, 1])

    def test_revers(self):
        self.assertEqual(self.conv.D_to_B_reverse(-73),[1, 0, 1, 1, 0, 1, 1, 0])

    def test_additional(self):
        self.assertEqual(self.conv.D_to_B_additional(-73),[1, 0, 1, 1, 0, 1, 1, 1])

    def test_IEE754(self):
        self.assertEqual(self.conv.D_to_B_IEE754(7.625),[0,1, 0, 0, 0, 0, 0, 0, 1,1.0, 1.0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

class Converter_to_D_Test(unittest.TestCase):
    def setUp(self):
        self.conv = Converter(8)
    
    def test_forward(self):
        self.assertEqual(self.conv.B_to_D_forward([0, 1, 0, 0, 1, 0, 0, 1]),73)

    def test_additional(self):
        self.assertEqual(self.conv.B_to_D_addtitioanl([1, 0, 1, 1, 0, 1, 1, 1]),-73)

    def test_IEEE754(self):
        self.assertEqual(self.conv.B_to_D_IEE754([0,1, 0, 0, 0, 0, 0, 0, 1,1.0, 1.0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),7.625)