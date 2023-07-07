
def fun(string):
    k = 0
    i = len(string)-1
    for j in string:
        if j == 'A':
            j = 10
        if j == 'B':
            j == 11
        else:
            j = int(j)
        k = k + j * (16** i)
        i = i -1
    return k

print(fun("5A"))

def summe(n):
    k = 0
    i = 0
    for i in range (0,n):
        k = k + 1.0/(2)**i        
    return k

print(summe(3))