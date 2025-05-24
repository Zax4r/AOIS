from constants import *
from functions import *


class Matrix:

    def __init__(self):
        self.matrix = []
        for _ in range(SIZE):
            self.matrix.append([0]*SIZE)

    def set_word_by_index(self,index,word):
        for i in range(SIZE):
            num = int(word[i])
            if 0<=num<=1:
                self.matrix[(i+index)%SIZE][index] = num

    def __str__(self):
        res = ""
        for i in self.matrix:
            res+=str(i)+'\n'
        return res
        
    def choose_2_colls(self):
        print(self)
        first = int(input('Выберете первый столбец(0-индексация): '))
        one = [self.matrix[i][first] for i in range(SIZE)]
        second = int(input('Выберете второй столбец(0-индексация): '))
        two = [self.matrix[i][second] for i in range(SIZE)]
        print('1.f2\n2.f7\n3.f8\n4.f13')
        choice = int(input('Выберете функцию: '))
        third = int(input('Выберете столбец, куда будет записан результат(0-индексация): '))
        match choice:
            case 1:
                res = f2(one,two)
            case 2:
                res = f7(one,two)
            case 3:
                res = f8(one,two)
            case 4:
                res = f13(one,two)
        self.set_word_by_index(third,res)

    def get_word_by_index(self,index):
        res = []
        for i in range(SIZE):
            res.append(self.matrix[(index+i)%SIZE][index])
        return res

    def compare(self,first,second):
        if first>=second:
            return 1
        if first<second:
            return -1
        

    def find_in_range(self,low,high):
        res = []
        for index in range(SIZE):
            word = self.get_word_by_index(index)
            converted = convert(word)
            g = self.compare(converted,low)
            l = self.compare(high,converted)
            if g==1:
                if l==1:
                    print(g,l)
                    res.append(word)
                    print(converted,low,high)

        return res      

    def ABVS(self,Vseek):
        for index in range(SIZE):
            word = self.get_word_by_index(index)
            V,A,B,S = word[:3],word[3:7],word[7:11],word[11:]
            if str(V)==str(Vseek):
                s_find = summ(A,B)
                self.set_word_by_index(index,V+A+B+s_find)
                    