import numpy as np
import matplotlib.pyplot as plt

def ggT_tumb(a,b):
    ggT = 1
    counter = 0
    for i in range (2,b+1):
        counter += 2
        a_i = a / i
        b_i = b / i
        if a_i == int(a_i) and b_i == int(b_i):
            ggT = i
    return (ggT, counter)

#print(ggT_tumb(10,120))

def ggt_tumbpp(a,b):
    counter = 0
    for i in range(b,0,-1):
        counter += 2
        a_i = a / i
        b_i = b / i
        if a_i == int(a_i) and b_i == int(b_i):
            return (i, counter)

#print(ggt_tumbpp(10,120))

def ggT_euclid(a,b):
    counter = 0
    m = a
    n = b
    while n > 0:
        counter +=1
        r = m % n
        m = n
        n = r
    return (m,counter)

#print(ggT_euclid(10,120))



def create_vektor(n, a= 100, b= 1000):
    return np.random.randint(a,b,size=n)




def main (n = 1000):
    a = create_vektor(n)
    b = create_vektor(n)

    k_ggT_tumb   = []
    k_ggt_tumbpp = []
    k_ggT_euclid = []

    for i in range (n):
        k_ggT_tumb.append  ( ggT_tumb(   a[i], b[i] )[1] )
        k_ggt_tumbpp.append( ggt_tumbpp( a[i], b[i] )[1] )
        k_ggT_euclid.append( ggT_euclid( a[i], b[i] )[1] )

    #print to histogram
    plt.xlabel('Vergleiche')
    plt.ylabel('Häufigkeiten')
    string = "ggT_tumb; k_min=",min(k_ggT_tumb), "k_max=",max(k_ggT_tumb)
    plt.title(string)
    plt.hist((k_ggT_tumb),bins=100)
    plt.savefig('hist_tumb.png')
    plt.clf()

    plt.xlabel('Vergleiche')
    plt.ylabel('Häufigkeiten')
    string = "ggT_tumb; k_min=",min(k_ggt_tumbpp), "k_max=",max(k_ggt_tumbpp)
    plt.title(string)
    plt.hist((k_ggt_tumbpp),bins=100)
    plt.savefig('hist_tumbpp.png')
    plt.clf()

    plt.xlabel('Vergleiche')
    plt.ylabel('Häufigkeiten')
    string = "ggT_tumb; k_min=",min(k_ggT_euclid), "k_max=",max(k_ggT_euclid)
    plt.title(string)
    plt.hist((k_ggT_euclid),bins=10)
    plt.savefig('hist_euclid.png')
 

    return (k_ggT_tumb,k_ggt_tumbpp,k_ggT_euclid)

main()