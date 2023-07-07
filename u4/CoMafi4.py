#tutorium


k = 0
def f(n):
    global k
    k=k+1

    if n==0:
        return k-1

    if n%3==0:
        return f(n+4)

    elif n%4==0:
        return f(n/2)

    else:  
        return f(n-1)


for n in range(0,100):
    k = 0
    print("n=",n,"k=",f(n))