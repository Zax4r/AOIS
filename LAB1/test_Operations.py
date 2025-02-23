import unittest
from Operations import Operations

class OperationsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum(self):
        s = Operations.sum([1, 1, 1, 0, 1, 0, 1, 0],[0, 0, 0, 0, 1, 1, 1, 0])
        self.assertEqual(s,[1, 1, 1, 1, 1, 0, 0, 0])
    
    def test_proiz(self):
        p = Operations.proiz([1, 0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 0, 1, 1, 1, 0])
        self.assertEqual(p,[1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0])
    
    def test_substruction(self):
        subs = Operations.substruction([1,0,0,0,0],[0,1])
        self.assertEqual(subs,[1,1,1,1])

    def test_delete_zeros(self):
        subs = Operations.delete_zeros([0,0,0,0,1])
        self.assertEqual(subs,[1])

    def test_add_zeros(self):
        subs1,subs2 = Operations.add_zeros([1,0,0,0,0],[0,1])
        self.assertEqual((subs1,subs2),([1,0,0,0,0],[0,0,0,0,1]))
        
    def test_delenie(self):
        de = Operations.delenie([1, 0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 0, 1, 1, 1, 0])
        self.assertEqual(de,[1, 0, 1, 1, 0, 0, 1, 0])

    def test_sum_IEE754(self):
        first = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1.0, 0.0, 0.0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        second = [0,1, 0, 0, 0, 0, 0, 0, 1,1.0, 1.0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s = Operations.sum_IEE754(first,second)
        self.assertEqual(s,[0,1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0,0.0, 1.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])