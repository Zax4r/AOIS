from Builder import Builder
from Binary_helper import Binary_helper
from constants import *
from Minimizator import Minimizator

def get_subtracktion():
    values = [0]*len(LITERALS)
    one = [0] * (len(LITERALS)-1) + [1]

    SDNF_Q1 = []
    SDNF_Q2 = []
    SDNF_Q3 = []
    print("",'  '.join(list(LITERALS[:-1])),end='  ')
    print("V Q1 Q2 Q3")
    for i in range(2**len(LITERALS)):
        print(values[:3],values[-1],end=' ')
        res = Binary_helper.sub_b(values[:-1],values[-1])
        print(values[:3])
        if res[0]:
            SDNF_Q1.append(Builder.build_SDNF(LITERALS[:3],values))
        if res[1]:
            SDNF_Q2.append(Builder.build_SDNF(LITERALS[:3],values))
        if res[2]:
            SDNF_Q3.append(Builder.build_SDNF(LITERALS[:3],values)) 
        values = res +[(1+i)%2]
        
    return SDNF_Q1,SDNF_Q2,SDNF_Q3

if __name__ == "__main__":
    SDNF_Q1,SDNF_Q2,SDNF_Q3 = get_subtracktion()
    print(SDNF_Q1,SDNF_Q2,SDNF_Q3,sep='\n')
    RES_Q1 = Minimizator.scleivanie_till_end_FORM(SDNF_Q1)[-1]
    RES_Q2 = Minimizator.scleivanie_till_end_FORM(SDNF_Q2)[-1]
    RES_Q3 = Minimizator.scleivanie_till_end_FORM(SDNF_Q3)[-1]
    print(RES_Q1,RES_Q2,RES_Q3,sep='\n')