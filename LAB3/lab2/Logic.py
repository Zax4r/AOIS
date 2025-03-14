from .Parser import Parser
from .Operands import Operands
from .ILogic import ILogic
from .Builder import Builder
from .Binary_helper import Binary_helper
from .constants import *


class Logic:

    def __init__(self):
        self.SDNF,self.SKNF = [],[]

    def solve(self, s: str):
        new_s = s
        while len(new_s) > 1:
            new_s = Operands.unary_operations(new_s)
            new_s = Operands.calculate_primitives(new_s)
            new_s = Parser.delete_brackets(new_s)
        return new_s
    
    def start(self):
        self.input_string = ILogic.get_string()
        self.input_string = self.input_string.replace("->",'>')
        self.SDNF,self.SKNF,res_bin,self.answer = [],[],[],[]
        SDNF_bin,SKNF_bin = [],[]
        self.arguments = Parser.get_arguments(self.input_string)
        self.arguments.sort()
        self.input_string = Parser.delete_tabulation(self.input_string)
        ILogic.print_arguments(self.arguments)
        for string,bits in Parser.work_w_str(self.input_string,self.arguments):
            res = self.solve(string)
            self.answer.append(int(res))
            if int(res):
                self.SDNF.append(Builder.build_SDNF(self.arguments,bits))
                SDNF_bin.append(Binary_helper.calculate(bits))
            else:
                self.SKNF.append(Builder.build_SKNF(self.arguments,bits))
                SKNF_bin.append(Binary_helper.calculate(bits))
            res_bin.append(int(res))
            ILogic.print_res(bits,res)
        #ILogic.print_decimal(Binary_helper.calculate(res_bin))
        SDNF_str,SKNF_str = "|".join(self.SDNF),"&".join(self.SKNF)
        ILogic.print_SKNF(SKNF_str,SKNF_bin)
        ILogic.print_SDNF(SDNF_str,SDNF_bin)


        
