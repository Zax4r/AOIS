from typing import List
from constants import *

class Minimizator:

    @staticmethod
    def check_if_neighbours(first: str, second: str):
        literals_f,literals_s = Minimizator.find_literals(first),Minimizator.find_literals(second)
        diff = literals_f.symmetric_difference(literals_s)
        if len(diff)!=2:
            return None
        a = diff.pop()
        b = diff.pop()
        if a[0] == "!" and a[1] != b[0]:
            return None
        if b[0] == "!" and b[1] != a[0]:
            return None
        if len(b)+len(a) == 2 and b[0]!=a[0]:
            return None
        return literals_f.intersection(literals_s)
                
    @staticmethod
    def check_form(FORM):
        for i in FORM:
            for j in i:
                if j in BINARY_OPERANDS:
                    return j
        return None
            
    @staticmethod
    def scleivanie(FORM, operand: str):
        length = len(FORM)
        with_neighbours = [0] * length
        new_FORM = []
        for i in range(length):
            for j in range(i+1,length):
                is_neighbour = Minimizator.check_if_neighbours(FORM[i],FORM[j])
                if is_neighbour is not None:
                    with_neighbours[j] = 1
                    with_neighbours[i] = 1
                    neighbor_excluded  = "("+operand.join(is_neighbour)+")"
                    new_FORM.append(neighbor_excluded)
        for i in range(len(with_neighbours)):
            if with_neighbours[i] == 0:
                new_FORM.append(FORM[i])
        return new_FORM
                           
    @staticmethod
    def scleivanie_till_end_FORM(FORM):
        steps = []
        operand = Minimizator.check_form(FORM)
        new_FORM = Minimizator.scleivanie(FORM,operand)
        end = False
        while not end:
            steps.append(set(new_FORM))
            old_FORM = new_FORM.copy()
            new_FORM = Minimizator.scleivanie(new_FORM,operand)
            end = old_FORM == new_FORM
        
        return steps
    
    @staticmethod
    def find_literals(form: str):
        literals = set()
        for i in range(len(form)):
            if form[i] in LITERALS:
                if form[i-1] == "!":
                    literals.add(f"!{form[i]}")
                else:
                    literals.add(form[i])
        return literals