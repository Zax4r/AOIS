from .constants import *
from typing import List

class ILogic:

    @staticmethod
    def get_string():
        print(f"Введите логичускую формулу \nАргументы:{LITERALS}\nОперанды:{BINARY_OPERANDS+UNARY_OPERANDS}")
        s = input()
        return s
    
    @staticmethod
    def print_res(bits: List[int], res: int):
        print(f"{bits} {res}")

    @staticmethod
    def print_arguments(args: List[str]):
        print(f"{args}")

    @staticmethod
    def print_SDNF(res: str, decimal: List[int]):
        print(f"СДНФ: {res}\nЧисленная форма: {decimal}")

    @staticmethod
    def print_SKNF(res: str, decimal: List[int]):
        print(f"СКНФ: {res}\nЧисленная форма: {decimal}")

    @staticmethod
    def print_decimal(res: int):
        print(f"Десятичная форма: {res}")