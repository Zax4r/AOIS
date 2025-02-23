from Composer import Composer
from test_Operations import OperationsTest
from test_Conventer import Converter_to_B_Test,Converter_to_D_Test
import unittest

MAX_BITS = 8

# a = [0]*32
# b = [0]*32
# a[7] = 1
# b[7] = 1
# print(Operations.sum_IEE754(a,b))

def main():
    Comp = Composer(MAX_BITS)
    Comp.read_number()
    Comp.read_number()
    Comp.sum()
    Comp.proiz()
    Comp.delenie()
    Comp.sum_IEE754()

if __name__ == "__main__":
    unittest.main()
