from Parser import Parser
from Operands import Operands
from ILogic import ILogic
from Builder import Builder
from Binary_helper import Binary_helper
from constants import *


class Logic:

    def solve(self, s: str):
        new_s = s
        while len(new_s) > 1:
            new_s = Operands.unary_operations(new_s)
            new_s = Operands.calculate_primitives(new_s)
            new_s = Parser.delete_brackets(new_s)
        return new_s
    
    def start(self):
        input_string = ILogic.get_string()
        SDNF,NSKF,res_bin = [],[],[]
        SDNF_bin,NSKF_bin = [],[]
        arguments = Parser.get_arguments(input_string)
        arguments.sort()
        input_string = Parser.delete_tabulation(input_string)
        ILogic.print_arguments(arguments)
        for string,bits in Parser.work_w_str(input_string,arguments):
            res = self.solve(string)
            if int(res):
                SDNF.append(Builder.build_SDNF(arguments,bits))
                SDNF_bin.append(Binary_helper.calculate(bits))
            else:
                NSKF.append(Builder.build_NSKF(arguments,bits))
                NSKF_bin.append(Binary_helper.calculate(bits))
            res_bin.append(int(res))
            ILogic.print_res(bits,res)
        ILogic.print_decimal(Binary_helper.calculate(res_bin))
        SDNF_str,NSKF_str = "|".join(SDNF),"&".join(NSKF)
        ILogic.print_NSKF(NSKF_str,NSKF_bin)
        ILogic.print_SDNF(SDNF_str,SDNF_bin)

        
