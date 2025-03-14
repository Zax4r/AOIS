from lab2.Binary_helper import Binary_helper

class Binary_helper_v2(Binary_helper):

    @staticmethod
    def convert_to_GRAY(number,count):
        b = [0] * count
        for i in range(count):
            b[i] = number%2
            number//= 2
        b.reverse()
        res = [0]*len(b)
        res[0] = b[0]
        for i in range(1,len(b)):
            res[i] = (b[i]+b[i-1])%2
        return  res
    
    