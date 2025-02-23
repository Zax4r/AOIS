from typing import List
DROB = 5

class Operations:

    @staticmethod
    def sum(first: List[int],second: List[int]) -> List[int]:
        res = [0] * len(first)
        add = 0
        for i in range(len(res)-1,-1,-1): 
            s = first[i]+second[i]+add
            res[i] = s%2
            add = s//2
        return res
    
    @staticmethod
    def proiz(first: List[int],second: List[int]) -> List[int]:
        res = [0] * (2 * len(first) - 1)
        znak = (first[0]+second[0])%2
        first[0],second[0] = 0,0
        add = 0
        for i in range(len(first)-1,-1,-1):
            if first[i] == 1:
                    for j in range(len(second)-1,-1,-1):
                        s = second[j]+add+res[i+j]
                        add = s//2
                        res[i+j] = s%2
        res[0] = znak
        return res

    @staticmethod
    def delete_zeros(number: List[int]) -> List[int]:
        for i in range(len(number)):
            if number[i] == 1:
                return number[i:]
        return number

    @staticmethod
    def add_zeros(first: List[int],second: List[int]) -> List[int]:
        if len(first)>len(second):
            return first, ([0]*(len(first) - len(second)) + second)
        else:
            return ([0]*(len(second) - len(first)) + first),second

    @staticmethod
    def substruction(umensh: List[int],vichit: List[int]) -> List[int]:
        vichitt = vichit.copy()
        umensht = umensh.copy()
        umensht,vichitt = Operations.add_zeros(first=umensht,second=vichitt)
        for i in range(len(umensht)):
            if umensht[i]>vichitt[i]:
                break
            if umensht[i]<vichitt[i]:
                return []
        
        for i in range(len(vichitt)):
            vichitt[i] = 1 if vichitt[i] == 0 else 0
        one = [0] * len(vichitt)
        one[len(vichitt)-1] = 1
        dopolnenie = Operations.sum(first=vichitt,second=one)
        s = Operations.sum(umensht,dopolnenie)
        return Operations.delete_zeros(s)

    @staticmethod
    def delenie(first: List[int],second: List[int]) -> List[int]:     
        res = []
        first +=[0]*(DROB)
        res.append((first[0]+second[0])%2)
        first[0],second[0] = 0,0
        try:
            if sum(second) == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Деление на 0!")
            exit(1)    
        first,second = Operations.delete_zeros(first),Operations.delete_zeros(second)
        var = first[:len(second)-1]
        for i in range(len(second)-1,len(first)):
            var.append(first[i])
            subs = Operations.substruction(var,second)
            if subs:
                res.append(1)
                var = subs
            else:
                res.append(0)
        
        return res 
    
    def sum_IEE754(first: List[int],second: List[int]) -> List[int]:
        if sum(first[1:]) == 0:
            return second
        
        if sum(second[1:]) == 0:
            return first

        exp1,exp2 = first[1:9],second[1:9]
        mant1,mant2 = [1]+first[9:],[1]+second[9:]
        diff = Operations.substruction(exp1,exp2)
        exp = exp1.copy()
        if diff == []:
            diff = Operations.substruction(exp2,exp1)
            exp = exp2.copy()

        diff = Operations.substruction(diff,[1])
        while diff:
            if exp == exp1:
                mant2 = mant2[:-1]
            else:
                mant1 = mant1[:-1]
            diff = Operations.substruction(diff,[1])
        mant1,mant2 = Operations.add_zeros(mant1,mant2)
        res = [0] * len(mant1)
        add = 0
        for i in range(len(res)-1,-1,-1): 
            s = mant1[i]+mant2[i]+add
            res[i] = s%2
            add = s//2
        if add:
            res = res[:23]
        else:
            res = res[1:24]
        if add:
            exp,add = Operations.add_zeros(exp,[add])
            exp = Operations.sum(add,exp)
        return [0]+exp+res


        

