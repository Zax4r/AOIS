import unittest
from test_functions import *
from matrix import Matrix

class test_Matrix(unittest.TestCase):

    def setUp(self):
        self.a = Matrix()
        self.d = [ ([1]*16,0),
        ([1]*16,2),
        ([0]*8+[1]*8,9)
        ]
        for i,idn in self.d:
            self.a.set_word_by_index(idn,i)

    def test_set_word(self):
        self.assertEqual(self.a.matrix[0][0],1)
        self.assertEqual(self.a.matrix[0][2],1)

    def test_get_word(self):
        self.assertEqual(self.a.get_word_by_index(0)[0],1)

    def test_ABVS(self):
        self.a.ABVS([1,1,1])
        self.assertEqual(self.a.matrix[0][0],1)
        self.assertEqual(self.a.matrix[0][2],0)

    def test_find_in_range(self):
        print(self.a)
        res = self.a.find_in_range(1,2**14)
        self.assertEqual(res[0],[0]*8+[1]*8)
    


if __name__=='__main__':
    unittest.main()