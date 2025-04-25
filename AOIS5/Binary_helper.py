from typing import List

class Binary_helper:
    
    @staticmethod
    def sum_b(first: List[int],second: List[int]) -> List[int]:
        res = [0] * len(first)
        add = 0
        for i in range(len(res)-1,-1,-1): 
            s = first[i]+second[i]+add
            res[i] = s%2
            add = s//2
        return res
    
    @staticmethod
    def calculate(bin: List[int]) -> int:
        res = 0
        for i in range(len(bin)):
            res *= 2
            res += bin[i]
        return res
    
    @staticmethod
    def sub_b(first: List[int],second: List[int]) -> List[int]:

        res = first.copy()
        add = second
        for i in range(len(res)-1,-1,-1): 
            res[i] = abs(res[i]-add)
            add = int(res[i]>first[i])
        return res
        
    