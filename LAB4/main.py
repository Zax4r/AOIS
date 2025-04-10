from Builder import Builder
from Binary_helper import Binary_helper
from constants import *
from Minimizator import Minimizator

def get_subtracktion():
    values = [0]*len(LITERALS)
    one = [0] * (len(LITERALS)-1) + [1]

    SDNF_D = []
    SDNF_B_1 = []

    for i in range(2**len(LITERALS)):
        D = sum(values)%2
        B_1 = int(sum(values[1:])>values[0])
        print(values,D,B_1)
        if D == 1:
            SDNF_D.append(Builder.build_SDNF(LITERALS,values))
        if B_1 == 1:
            SDNF_B_1.append(Builder.build_SDNF(LITERALS,values))  
        values = Binary_helper.sum_b(values,one)
        
    SDNF_D = Minimizator.scleivanie_till_end_FORM(SDNF_D)[-1]
    SDNF_B_1 = Minimizator.scleivanie_till_end_FORM(SDNF_B_1)[-1]
    return "|".join(SDNF_D),  "|".join(SDNF_B_1)

def get_D8421_1():
    values = [0]*LEN_OF_TETRADA
    one = [0]*(LEN_OF_TETRADA-1)+[1]
    for i in range(10):
        res = Binary_helper.sum_b(values,one)
        print(*values,'\t\t',*res)
        values = res

if __name__ == "__main__":
    SDNF_D,SDNF_B_1 = get_subtracktion()
    print("СДНФ для D: "+SDNF_D,"СДНФ для В+1: "+SDNF_B_1,sep  = '\n')
    get_D8421_1()