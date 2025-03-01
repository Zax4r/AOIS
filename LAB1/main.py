from Composer import Composer
from test_Operations import OperationsTest
from test_Conventer import Converter_to_B_Test,Converter_to_D_Test
import unittest

def main():
    Comp = Composer()
    Comp.read_number()
    Comp.read_number()
    Comp.sum()
    Comp.proiz()
    Comp.delenie()
    Comp.sum_IEE754()
    

if __name__ == "__main__":
    unittest.main()
