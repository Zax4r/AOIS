from lab2.Logic import Logic
from Minimizator import Minimizator
from ILogic_v2 import ILogic_v2
from Binary_helper_v2 import Binary_helper_v2
from lab2.Parser import Parser

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
        raschet_SDNF = Minimizator.scleivanie_till_end_FORM(self.SDNF)
        raschet_SDNF.append(set(self.delete_useless(raschet_SDNF[-1],'|')))
        ILogic_v2.print_raschetn(raschet_SDNF)
        tabl_taschet_SDNF = Minimizator.rasch_tabl(self.SDNF,raschet_SDNF[-1])
        ILogic_v2.print_tabl_raschetn(tabl_taschet_SDNF)
        raschet_SKNF = Minimizator.scleivanie_till_end_FORM(self.SKNF)
        raschet_SKNF.append(set(self.delete_useless(raschet_SKNF[-1],'&')))
        ILogic_v2.print_raschetn(raschet_SKNF)
        tabl_taschet_SKNF = Minimizator.rasch_tabl(self.SKNF,raschet_SKNF[-1])
        ILogic_v2.print_tabl_raschetn(tabl_taschet_SKNF)
        try:
            self.build_matrix()
            ILogic_v2.print_matrix(self.matrix,raschet_SKNF[-1],raschet_SDNF[-1],self.argsY,self.argsX)
        except ValueError:
            ILogic_v2.print("Всего один элемент")

            
    def delete_useless(self,FORM,oper):
        FORM = list(FORM)

        to_minim = FORM.copy()
        def delete_one(self,to_minim):
            for i in range(len(to_minim)):
                answer = []
                part = to_minim[:i]+to_minim[i+1:]
                str = oper.join(part)
                for string,_ in Parser.work_w_str(str,self.arguments):
                        res = self.solve(string)
                        answer.append(int(res))   
                if self.answer == answer:
                    return part
            return to_minim
        
        while True:
            res = delete_one(self,to_minim)
            if res == to_minim:
                break
            to_minim = res
        return to_minim


       