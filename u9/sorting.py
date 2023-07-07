import random
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
quick_counter = 0
merge_counter = 0

def reisverschluss(liste_1, liste_2):
    global merge_counter
    result = []
    while liste_1 != [] and liste_2 != []:
        merge_counter += 1
        if liste_1[0] <= liste_2[0]:
            result.append(liste_1[0]) 
            liste_1 = liste_1[1:]
        else:
            result.append(liste_2[0]) 
            liste_2 = liste_2[1:]
    return (result + liste_1 + liste_2)

def mergesort(liste):
    n = len(liste)
    if n == 1:
        return liste
    return reisverschluss(mergesort( liste[:round(n/2)] ),mergesort( liste[round(n/2):] ))

def mergesort_counter(liste):
    global merge_counter
    merge_counter = 0
    return (mergesort(liste), merge_counter)

def bubblesort (liste):
    vergleiche=0
    swap = True
    n = len(liste)-1
    while swap:
        swap = False
        for i in range(n):
            vergleiche += 1
            if liste[i]>liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                swap = True
    n = n-1
    return (liste,vergleiche)

def partition(liste):
    global quick_counter
    middl = liste[0]
    left =  []
    right = []
    for i in range(1,len(liste)):
        item = liste[i]
        quick_counter += 1
        if middl <= item:
            right.append(item)
        else:
            left.append(item)
    return (left, [middl], right)

def quicksort(liste):
    if liste == []:
        return []
    left, middl, right = partition(liste)
    return quicksort(left) + middl + quicksort(right)

def quicksort_counter(liste):
    global quick_counter
    quick_counter = 0
    return (quicksort(liste), quick_counter)

def main():
    max_bubl, min_bubl, avg_bubl = [], [], []
    max_merg, min_merg, avg_merg = [], [], []
    max_quic, min_quic, avg_quic = [], [], []
    n_list = []

    for k in range(1,4):
        print(k)
        n = 10**k
        n_list.append(n)
        temp_bubl = []
        temp_merg = []
        temp_quic = []
        for _ in range(100):
            random_list = [random.randint(0,1) for i in range(n)]
            res = bubblesort(random_list)
            temp_bubl.append(res[1])

            random_list = [random.randint(0,1) for i in range(n)]
            res = mergesort_counter(random_list)
            temp_merg.append(res[1])

            random_list = [random.randint(0,1) for i in range(n)]
            res = quicksort_counter(random_list)
            temp_quic.append(res[1])

        n = n_list[-1]
        max_bubl.append(max(temp_bubl))
        min_bubl.append(min(temp_bubl))
        avg_bubl.append(sum(temp_bubl)/100)

        max_merg.append(max(temp_merg))
        min_merg.append(min(temp_merg))
        avg_merg.append(sum(temp_merg)/100)

        max_quic.append(max(temp_quic))
        min_quic.append(min(temp_quic))
        avg_quic.append(sum(temp_quic)/100)


    plt.xlabel('n')
    plt.ylabel('Vergleiche')
    plt.title("red:bubbl, blue:merg, green:quic")
    plt.axis([0, n_list[-1], 0, 100000])
    plt.plot(n_list, avg_bubl, 'r')
    plt.plot(n_list, avg_merg, 'b')
    plt.plot(n_list, avg_quic, 'g')
    plt.savefig('bubbl_merg_quic_avg.png')
    plt.clf()

    plt.xlabel('n')
    plt.ylabel('Vergleiche')
    plt.title("red:max, blue:min, green:avg")
    plt.plot(n_list, max_bubl, ':r')
    plt.plot(n_list, min_bubl, '--b')
    plt.plot(n_list, avg_bubl, 'g')
    plt.savefig('bubbl.png')
    plt.clf()

    plt.xlabel('n')
    plt.ylabel('Vergleiche')
    plt.title("red:max, blue:min, green:avg")
    plt.plot(n_list, max_merg, ':r')
    plt.plot(n_list, min_merg, '--b')
    plt.plot(n_list, avg_merg, 'g')
    plt.savefig('merg.png')
    plt.clf()

    plt.xlabel('n')
    plt.ylabel('Vergleiche')
    plt.title("red:max, blue:min, green:avg")
    plt.plot(n_list, max_quic, ':r')
    plt.plot(n_list, min_quic, '--b')
    plt.plot(n_list, avg_quic, 'g')
    plt.savefig('quic.png')
    plt.clf()



main()

