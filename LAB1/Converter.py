from typing import List
from Operations import Operations
from constants import *
class Converter:

    def __init__(self):
        self.MAX_BITS = MAX_BITS
   
    def D_to_B_forward(self,decimal: int) -> List[int]:
        res = [0] * self.MAX_BITS
        znak = 0 if decimal>=0 else 1
        decimal = abs(decimal)
        for index in range(len(res)):
            res[index] = decimal%2
            decimal = decimal//2
        res.reverse()
        res[0] = znak
        return res

    def D_to_B_reverse(self,decimal: int) -> List[int]:
        res = self.D_to_B_forward(decimal=decimal)
        if decimal<0:
            for i in range(1,len(res)):
                res[i] = 0 if res[i]==1 else 1
        return res

    def D_to_B_additional(self,decimal: int) -> List[int]:
        if decimal<0:
            b = self.D_to_B_reverse(decimal=decimal)
            one = self.D_to_B_forward(1)
            res = Operations.sum(b,one)
        else:
            res = self.D_to_B_forward(decimal=decimal)
        return res
        
    def B_to_D_forward(self,bin: List[int]) -> int:
        res = 0
        for i in range(1,len(bin)):
            res *= 2
            res += bin[i]
        return res if bin[0] == 0 else -res
    
    def B_to_D_addtitioanl(self,bin: List[int]) -> int:
        if bin[0] == 0:
            return self.B_to_D_forward(bin)
        else:
            for i in range(0,len(bin)):
                bin[i] = 0 if bin[i]==1 else 1
            res = Operations.sum(bin,self.D_to_B_forward(1))
            return -self.B_to_D_forward(res)
        
    def B_to_D_delenie(self,bin: List[int]) ->float:
        tbin = bin.copy()
        znak = tbin[0]
        tbin[0] = 0
        base = 2 ** (-DROB)
        res = 0
        for i in range(len(tbin)-1,0,-1):
            res +=base*tbin[i]
            base *=2

        return -res if znak else res   
    
    def B_to_D_IEE754(self,bin: List[int]) -> float:
        if sum(bin) == 0:
            return 0
        
        poryadok =[0] + bin[1:9]
        deci_poryadok = self.B_to_D_forward(poryadok) - EXP_CONST
        if deci_poryadok == (EXP_CONST+1):
            return "-Inf" if bin[0] else "Inf"
        
        mant = [1]+bin[9:]
        deci_mant = 0
        base = 1
        for i in range(len(mant)):
            deci_mant += mant[i] * base
            base /= 2
  
        return deci_mant * (2**deci_poryadok)

    def D_to_B_IEE754(self,number: float) -> List[int]:
        celaya,drobnaya = number//1,number%1
        if number == 0:
            return [0]*IEEE754_LEN
        
        celaya_b = []
        drobnaya_b = []
        while celaya>0 and (len(drobnaya_b)+len(celaya_b))<IEEE754_LEN:
            celaya_b.append(celaya%2)
            celaya = celaya//2
        celaya_b.reverse()

        while drobnaya > 0 and (len(drobnaya_b)+len(celaya_b))<IEEE754_LEN :
            drobnaya *= 2
            drobnaya_b.append(int(drobnaya//1))
            drobnaya = drobnaya%1

        if not celaya_b:
            old_len = len(drobnaya_b)
            drobnaya_b = Operations.delete_zeros(drobnaya_b)
            shift = len(drobnaya_b) - old_len
            mant = drobnaya_b[1:]  
            exp = shift-1 
        else:
            mant = celaya_b[1:] + drobnaya_b
            exp = len(celaya_b) - 1  


        mant = mant + ([0] * (MANT_LEN - len(mant)))

        exp_real = exp + EXP_CONST
        exp_b = []
        while exp_real > 0:
            exp_b.append(exp_real % 2)
            exp_real //= 2
        exp_b.reverse()

        exp_b = [0] * (MAX_BITS - len(exp_b)) + exp_b

        res = [0] + exp_b + mant
        return res[:IEEE754_LEN]


        