from lab2.Logic import Logic
from Minimizator import Minimizator
from ILogic_v2 import ILogic_v2
from Binary_helper_v2 import Binary_helper_v2
from lab2.Parser import Parser
from itertools import product
from copy import deepcopy

class Logic_v2(Logic):

    def __init__(self):
        super().__init__()

    def work_w_str(self,s,args):
        for i in range(2**len(args)):
            bits = Binary_helper_v2.convert_to_GRAY(i,len(args))
            new_s = s
            for j in range(len(args)):
                new_s = new_s.replace(args[j],str(bits[j]))
            yield new_s,bits,i
            
    def build_matrix(self):
        if len(self.arguments)<2:
            raise ValueError
        LargsY,LargsX = len(self.arguments)//2,(len(self.arguments)+1)//2
        argsY,argsX = self.arguments[:LargsY],self.arguments[LargsY:]
        self.ones,self.zeros = 0,0
        matrix = []
        for i in range(2**LargsY):
            matrix.append([0]*(2**LargsX))
        
        for part_s,_,i in self.work_w_str(self.input_string,argsY):
            for s,_,j in self.work_w_str(part_s,argsX):
                matrix[i][j] = int(self.solve(s))
                
        self.matrix = matrix
        self.argsY,self.argsX = argsY,argsX

    def start(self):
        super().start()


        ILogic_v2.print("SDNF RASCHET")
        raschet_SDNF = Minimizator.scleivanie_till_end_FORM(self.SDNF)
        tupic_SDNF_ras = set(self.delete_useless_RAS(list(raschet_SDNF[-1]),'|'))
        result_SDNF = raschet_SDNF
        if raschet_SDNF[-1].difference(tupic_SDNF_ras):
            result_SDNF = raschet_SDNF + [tupic_SDNF_ras]
        ILogic_v2.print_raschetn(result_SDNF)

        ILogic_v2.print("SDNF RASCHET-TABLE")
        tabl_raschet_SDNF = Minimizator.rasch_tabl(self.SDNF,raschet_SDNF[-1])
        tupic_SDNF_ras_tabl = self.delete_useless_RAS_TABL(tabl_raschet_SDNF)
        ILogic_v2.print_tabl_raschetn(tupic_SDNF_ras_tabl,original = raschet_SDNF[-1])

        ILogic_v2.print("SKNF RASCHET")
        raschet_SKNF = Minimizator.scleivanie_till_end_FORM(self.SKNF)
        tupic_SKNF_ras = set(self.delete_useless_RAS(list(raschet_SKNF[-1]),'&'))
        result_SKNF = raschet_SKNF
        if raschet_SKNF[-1].difference(tupic_SKNF_ras):
            result_SKNF = raschet_SKNF + [tupic_SKNF_ras]
        ILogic_v2.print_raschetn_SKNF(result_SKNF)

        ILogic_v2.print("SKNF RASCHET-TABLE")        
        tabl_taschet_SKNF = Minimizator.rasch_tabl(self.SKNF,raschet_SKNF[-1])
        tupic_SKNF_ras_tabl = self.delete_useless_RAS_TABL(tabl_taschet_SKNF)
        ILogic_v2.print_tabl_raschetn(tupic_SKNF_ras_tabl,original = raschet_SKNF[-1])

        try:
            self.build_matrix()
            self.true_matrix = self.matrix.copy()
            self.delete_useless_Karno()
            ILogic_v2.print_matrix(self.true_matrix,self.FINAL_SDNF_KARNO,self.FINAL_SKNF_KARNO,self.argsY,self.argsX)
        except ValueError:
            ILogic_v2.print("Всего один элемент")

            
    def delete_useless_RAS(self,FORM,oper):
        to_minim = FORM.copy()    
        variants_to_check = self.delete_one(to_minim,oper)
        variants_recievd = []
        for i in range(len(FORM)):
            for form in variants_to_check:
                variants_recievd += self.delete_one(form,oper)
            variants_to_check = variants_recievd.copy()
            variants_recievd.clear()
        return min(variants_to_check,key=lambda x:len(x))

    def delete_one(self,to_minim,oper):
        all_combinations = []
        if len(to_minim) <= 1:
            return to_minim
        to_minim = to_minim.copy()
        changed = False
        for i in range(len(to_minim)):
            answer = []
            part = to_minim[:i]+to_minim[i+1:]
            str = oper.join(part)
            for string,_ in Parser.work_w_str(str,self.arguments):
                    res = self.solve(string)
                    answer.append(int(res))   
            if self.answer == answer:
                changed = True
                all_combinations.append(part)
        if not changed:
            return [to_minim]
        else:
            return all_combinations


    def delete_useless_RAS_TABL(self,FORM):
        res1 = FORM.copy()

        def deleter(res,items):
            res = res.copy()
            for i in items:
                our_constituents = i[1]
                values = our_constituents.copy()
                for j in items:
                    if i[0] != j[0]:
                        their_constituents = j[1]
                        if their_constituents.issubset(our_constituents):
                            res.pop(i[0])
                            return res
                        values = values.difference(their_constituents)
                if values == set([]):
                    res.pop(i[0])
                    return res
            return res

        new = deleter(res1,res1.items())
        while new != res1:
            res1 = new
            new = deleter(res1,res1.items())
        return new


    def delete_useless_Karno(self):
        self.convert_matrix()
        SDNF = self.build_form('&',False)
        SKNF = self.build_form("|",True)
        self.FINAL_SDNF_KARNO = SDNF
        self.FINAL_SKNF_KARNO = SKNF

    def build_form(self,operand,zeros):
        res = []
        if not zeros:
            final = self.find_rows_colls(self.new_matrix,self.matrix_checked,zeros)
        else:
            final = self.find_rows_colls(self.new_matrix,self.matrix_checked2,zeros)                
        print(final)
        for start_row,row_amount,start_col,col_amount in final:
            if start_row == 0:
                start_row = len(self.matrix)
            if start_col == 0:
                start_col = len(self.matrix[0])
            start_row,start_col = start_row-1,start_col-1
            start_Y = Binary_helper_v2.convert_to_GRAY(start_row,len(self.argsY))
            equal_indexes_Y = set([i for i in enumerate(start_Y)])
            for j in range(row_amount):
                end_Y = Binary_helper_v2.convert_to_GRAY((start_row+j)%len(self.matrix) ,len(self.argsY))
                equal_indexes_Y = equal_indexes_Y.intersection(set([i for i in enumerate(end_Y)]))

            start_X = Binary_helper_v2.convert_to_GRAY(start_col+0,len(self.argsX))
            equal_indexes_X = set([i for i in enumerate(start_X)])
            for j in range(col_amount):
                end_X = Binary_helper_v2.convert_to_GRAY((start_col+j)%len(self.matrix[0]) ,len(self.argsX))
                equal_indexes_X = equal_indexes_X.intersection(set([i for i in enumerate(end_X)]))

            arguments = []
            for index,value in equal_indexes_Y:
                if (value == 0 and zeros) or (value == 1 and not zeros):
                    arguments.append(f"{self.argsY[index]}")
                else:
                    arguments.append(f"!{self.argsY[index]}")

            for index,value in equal_indexes_X:
                if   (value == 0 and zeros) or (value == 1 and not zeros):
                    arguments.append(f"{self.argsX[index]}")
                else:
                    arguments.append(f"!{self.argsX[index]}")
            res.append('('+ operand.join(arguments)+')')
        return list(set(res))
    
    def convert_matrix(self):
        self.new_matrix = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            self.new_matrix[i].insert(0,self.matrix[i][-1])
        self.new_matrix.insert(0,self.new_matrix[-1])  
        self.matrix_checked =deepcopy(self.new_matrix)
        self.matrix_checked2 = deepcopy(self.matrix_checked)
        for i in range(len(self.matrix_checked2)):
            for j in range(len(self.matrix_checked2[i])):
                self.matrix_checked2[i][j] = 0 if self.matrix_checked[i][j] else 1

    def find_rows_colls(self,matrix,matrix_checked,zeros):
        final = []
        rows_amount_overall,colls_amount_overall = len(matrix),len(matrix[0])
        rows_widths = []
        width = 1
        while width < rows_amount_overall:
            rows_widths.append(width)
            width*=2
        
        colls_widths = []
        width = 1
        while width < colls_amount_overall:
            colls_widths.append(width)
            width*=2
        
        pairs = list(product(rows_widths,colls_widths))
        pairs.sort(key = lambda x:x[1]*x[0])
        while pairs:
            row_width,colls_width = pairs[-1]
            pairs.pop()
            final,matrix_checked = self.calculate_all_submatrixes(row_width,colls_width,matrix,matrix_checked,final,zeros)
        return final

    def calculate_all_submatrixes(self,row_amount,column_amount,matrix,matrix_checked,final,zeros):
        number_of_rows,number_of_colls = len(matrix)-row_amount+1,len(matrix[0])-column_amount+1
        for start_row in range(number_of_rows):
            for start_coll in range(number_of_colls):
                valid,matrix_checked = self.sum_sub_matrix(start_row,row_amount,start_coll,column_amount,matrix,matrix_checked,zeros)
                if valid:
                    final.append((start_row,row_amount,start_coll,column_amount))
        return final,matrix_checked

    def sum_sub_matrix(self,row_start,row_amount,column_start,column_amount,matrix,matrix_checked,zeros):
        res = 0
        checked = 0
        target = 0
        for i in range(row_start,row_start+row_amount):
            for j in range(column_start,column_start+column_amount):
                res += matrix[i][j]
                target += 1
                checked += matrix_checked[i][j]
        
        if checked == 0:
            return False,matrix_checked

        if (target == res and not zeros) or (zeros and res == 0):
            for i in range(row_start,row_start+row_amount):
                for j in range(column_start,column_start+column_amount):
                    matrix_checked[i][j] = 0

            if row_start == 0:
                for j in range(column_start,column_start+column_amount):
                    matrix_checked[-1][j]=0

            if row_start+row_amount > len(matrix_checked)-1:
                for j in range(column_start,column_start+column_amount):
                    matrix_checked[0][j]=0

            if column_start == 0:
                for i in range(row_start,row_start+row_amount):
                    matrix_checked[i][-1]=0

            if column_start+column_amount > len(matrix_checked)-1:
                for i in range(row_start,row_start+row_amount):
                    matrix_checked[i][0]=0

            return True,matrix_checked

        return False,matrix_checked
        

            

    

       