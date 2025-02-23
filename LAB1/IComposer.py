from typing import List,Tuple

class IComposer:

    @staticmethod
    def input_number(size: int) -> int:
        print(f"Введите число №{size+1}:")
        inp = int(input())
        return inp
    
    @staticmethod
    def print_varies(numbers:Tuple[int,List[int],List[int],List[int]]):
        print(f"В десятичном     {numbers[0]}")
        print(f"В прямом         {numbers[1]}")
        print(f"В обратном       {numbers[2]}")
        print(f"В дополнительном {numbers[3]}",end="\n\n")

    @staticmethod
    def print_proiz(number: int, bin: List[int]):
        print(f"В десятичном     {number}")
        print(f"В прямом         {bin}")
    
    @staticmethod
    def print_delenie(number: float,bin: List[int]):
        print(f"В десятичном     {number}")
        print(f"В прямом         {bin}")

    @staticmethod
    def read_IEE():
        print(f"Введите число:")
        Iee = float(input())
        return Iee
    
    @staticmethod
    def print_IEE_sum(bin: List[int], number:float):
        print(f"В десятичном     {number}")
        print(f"В прямом         {bin[0],bin[1:9],bin[9:]}")