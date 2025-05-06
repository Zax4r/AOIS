import unittest
from Table import Table

class Table_Test(unittest.TestCase):
    def setUp(self):
        self.table = Table()
    
    def test_add(self):
        self.table['Moskow']='1'
        
        self.assertEqual(self.table['Moskow'],'1')

    def test_update(self):
        self.table['Moskow']='1'
        self.table['Moskow']='2'
        self.assertEqual(self.table['Moskow'],'2')
    
    def test_key_error(self):
        with self.assertRaises(KeyError):
            self.table['Moskow']

    def test_delete(self):
        self.table['Moskow'] = 100
        del self.table['Moskow']
        with self.assertRaises(KeyError):
            self.table['Moskow']
        
    def test_collision(self):
        self.table['Moskow'] = "1"
        self.table['Mozir'] = '2'
        self.assertEqual(self.table['Mozir'],'2')