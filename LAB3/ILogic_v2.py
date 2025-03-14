from typing import List,Dict
from Binary_helper_v2 import Binary_helper_v2


class ILogic_v2:

    @staticmethod
    def print_raschetn(res: List):
        print("SDNF")
        for i in range(len(res)):
            final = "|".join(res[i])
            print(f"Step{i+1}: {final}")

    @staticmethod
    def print_raschetn_SKNF(res: List):
        print("SKNF")
        for i in range(len(res)):
            final = "&".join(res[i])
            print(f"Step{i+1}: {final}")

    @staticmethod
    def print_tabl_raschetn(res: Dict):
        values = set()
        for value in res.values():
            for v in value:
                values.add(v)

        print(end=" "*8)
        for key in res.keys():
            print(' '+str(key),end='  ')
        print()

        for val in values:
            print(f"{val}"+(8-len(val))*' ',end="")
            for key in res.keys():
                if val in res[key]:
                    print(' '*(len(key)//2 + 1) +  "+" + ' '*(len(key)//2 + 1),end="")
                else:
                    print(' '*(len(key)//2 + 1) +  "-" + ' '*(len(key)//2 + 1),end="")
            print()
        print(end='\n\n')

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
        f = "&".join(f)
        s = "|".join(s)
        print("SKNF:",f)
        print("SDNF:",s)

    def print(s: str):
        print(s)


    