from Converter import Converter
from Operations import Operations
from IComposer import *
from typing import List,Tuple

class Composer:

    def __init__(self,MaxBits: int):
        self.MAXBITS = MaxBits
        self.conv = Converter(MaxBits)
        self.numbers = []
        self.forward = []
        self.reversed = []
        self.additional = []

    def read_number(self):
        self.numbers.append(IComposer.input_number(len(self.numbers)))
        self.convert_all(self.numbers[-1], save=True)
    
    def convert_all(self,number: int, save: bool):
        forward = self.conv.D_to_B_forward(number)
        revers = self.conv.D_to_B_reverse(number)
        additional = self.conv.D_to_B_additional(number)
        if save:
            self.forward.append(forward)
            self.reversed.append(revers)
            self.additional.append(additional)
        self.print_number((number,forward,revers,additional))

    def print_number(self, numbers:Tuple[int,List[int],List[int],List[int]]):
        IComposer.print_varies(numbers)

    def sum(self):
        first = self.additional[-2].copy()
        second = self.additional[-1].copy()
        s = Operations.sum(first=first,second=second)
        s = self.conv.B_to_D_addtitioanl(s)
        self.convert_all(s, save = False)

    def proiz(self):
        first = self.forward[-2].copy()
        second = self.forward[-1].copy()
        p = Operations.proiz(first=first,second=second)
        decimal = self.conv.B_to_D_forward(p)
        IComposer.print_proiz(decimal,p)

    def delenie(self):
        first = self.forward[-2].copy()
        second = self.forward[-1].copy()
        d = Operations.delenie(first=first,second=second)
        decimal = self.conv.B_to_D_delenie(d)
        IComposer.print_delenie(decimal,d)

    def sum_IEE754(self):
        first = IComposer.read_IEE()
        second = IComposer.read_IEE()
        first_conv,second_conv = self.conv.D_to_B_IEE754(first),self.conv.D_to_B_IEE754(second)
        res = Operations.sum_IEE754(first_conv,second_conv)
        res_d = self.conv.B_to_D_IEE754(res)
        IComposer.print_IEE_sum(res,res_d)