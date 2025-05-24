
def f7(first,second):
    res = [0]*len(first)
    for i in range(len(first)):
        res[i] = int(first[i] or second[i])

    return res

def f8(first,second):
    res = [0]*len(first)
    for i in range(len(first)):
        res[i] = int(not (first[i] or second[i]))

    return res

def f2(first,second):
    res = [0]*len(first)
    for i in range(len(first)):
        res[i] = int(first[i] and  not second[i])

    return res

def f13(first,second):
    res = [0]*len(first)
    for i in range(len(first)):
        res[i] = int(not first[i] or second[i])

    return res

def summ(first,second):
    res = [0]+first
    for i in range(len(res)-1,0,-1):
        res[i] = (res[i]+second[i-1])%2
        b = (res[i]+second[i-1])//2
    res[0] = b
    return res

def convert(form):
    a = 0
    for numb in form:
        a+=numb
        a*=2
    return a//2