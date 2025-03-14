from unittest import TestCase
from Binary_helper_v2 import Binary_helper_v2


class test_Bing_help_2(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_GRAY(self):
        i = 2
        res = Binary_helper_v2.convert_to_GRAY(i,2)
        self.assertEqual([1,1],res)