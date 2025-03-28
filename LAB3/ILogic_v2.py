from typing import List,Dict
from Binary_helper_v2 import Binary_helper_v2


class ILogic_v2:

    @staticmethod
    def print_raschetn(res: List):
        for i in range(len(res)):
            final = "|".join(res[i])
            print(f"Step{i+1}: {final}")
        ILogic_v2.print()

    @staticmethod
    def print_raschetn_SKNF(res: List):
        for i in range(len(res)):
            final = "&".join(res[i])
            print(f"Step{i+1}: {final}")
        ILogic_v2.print()        

    @staticmethod
    def print_tabl_raschetn(res: Dict, original = List):
        print(f"Конец этапа склеивания: {original}")

        values = set()
        for value in res.values():
            values = values.union(value)

        print(end=" "*8)
        for val in values:
            print(' '+str(val),end='  ')
        print()

        for key in res.keys():
            print(f"{key}"+(8-len(key))*' ',end="")
            for val in values:
                if val in res[key]:
                    print(' '*(len(val)//2 + 1) +  "+" + ' '*(len(val)//2 + 1),end="")
                else:
                    print(' '*(len(val)//2 + 1) +  "-" + ' '*(len(val)//2 + 1),end="")
            print()
        ILogic_v2.print()

    @staticmethod
    def print_matrix(matrix,f,s,argsY,argsX):
        print(*argsY,'\\',*argsX,end="\t",sep='')
        for i in range(2**(len(argsX))):
            grey_kod = Binary_helper_v2.convert_to_GRAY(i,len(argsX))
            print(grey_kod,end=' ')
        print()
        for i in range(2**(len(argsY))):
            grey_kod = Binary_helper_v2.convert_to_GRAY(i,len(argsY))
            print(grey_kod,end='\t')
            for elem in matrix[i]:
                print(elem,end = '\t')
            print()
        print("result SDNF:","|".join(f))
        print("result SKNF:","&".join(s))
        ILogic_v2.print()

    def print(s: str = ""):
        print(f"{s}\n***********************************",end="\n")


    