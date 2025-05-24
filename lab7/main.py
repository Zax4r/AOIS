from matrix import *


if __name__=='__main__':
    a = Matrix()
    d = [ ([1]*16,0),
    ([1]*16,2)
    ]
    for i,idn in d:
        a.set_word_by_index(idn,i)

    a.choose_2_colls()   
    a.ABVS([1,1,1]) 
    print(a)