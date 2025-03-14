from unittest import TestCase
from Minimizator import Minimizator

class test_Minimizator(TestCase):
    def setUp(self):
        return super().setUp()

    def test_scleivanie(self):
        test = ['(!a&b&c)', '(a&!b&c)', '(a&b&c)']
        res = Minimizator.scleivanie_till_end_FORM(test)
        res = list(res).sort()
        tes = ["(a&c)","(c&b)"].sort()
        self.assertEqual(res,tes)