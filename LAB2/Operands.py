from constants import *
import re

class Operands:

    @staticmethod
    def unary_operations(s: str):
        new_s = s
        while (("!0" in new_s) or ("!1" in new_s)):
            new_s = new_s.replace("!0","1")
            new_s = new_s.replace("!1","0")
        return new_s
    
    @staticmethod
    def calculate(i: str):
        match i[1]:
            case "&":
                return int(i[0]) & int(i[2])
            case "|":
                return int(i[0]) | int(i[2])
            case ">":
                return int(int(i[0]) <= int(i[2]))
            case "~":
                return int(int(i[0]) == int(i[2]))

    @staticmethod
    def calculate_primitives(s: str):
        new_s = s
        for i in re.findall(rf"[01][{BINARY_OPERANDS}][01]",new_s):
            res = Operands.calculate(i)
            new_s = new_s.replace(i,str(res))
        return new_s
    
