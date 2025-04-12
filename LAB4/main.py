from Builder import Builder
from Binary_helper import Binary_helper
from constants import *
from Minimizator import Minimizator

def get_subtracktion():
    values = [0]*len(LITERALS)
    one = [0] * (len(LITERALS)-1) + [1]

    SDNF_D = []
    SDNF_B_1 = []
    print(LITERALS,"DP",sep='\t')
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
    print('D8421\t\t\tD8421+1')
    for i in range(10):
        res = Binary_helper.sum_b(values,one)
        print(*values,'\t\t',*res)
        values = res

def replace(form):
    form =form.replace("X1","A")
    form = form.replace("X2","B")
    form =form.replace("X3","C")
    form = form.replace("X4","D")
    return form

def replace_back(form):
    for i,l in enumerate(list(LITERALS),start=1):
        form = form.replace(l,f"X{i}")
    return form

if __name__ == "__main__":
    SDNF_D,SDNF_B_1 = get_subtracktion()
    print("СДНФ для D: "+SDNF_D,"СДНФ для В+1: "+SDNF_B_1,sep  = '\n')
    print()
    get_D8421_1()
    print("Y1 = !X1")
    
    res = replace("(X1&!X2)|X2&!X1)")
    constitunets = Minimizator.scleivanie_till_end_FORM(res.split("|"))[-1]
    print("Y2 =",replace_back("|".join(constitunets)))
    
    res = replace("(X2|X3)&(!X2|!X1|!X3)&(X1|X3)")
    constitunets = Minimizator.scleivanie_till_end_FORM(res.split("&"))[-1]
    print("Y3 =",replace_back("&".join(constitunets)))
    
    res = replace("X4|(X1&X2&X3)")
    constitunets = Minimizator.scleivanie_till_end_FORM(res.split("|"))[-1]
    print("Y4 =",replace_back("|".join(constitunets)))