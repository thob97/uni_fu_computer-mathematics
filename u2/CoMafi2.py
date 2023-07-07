
#tutorium
from random import randint

def lotto():
    dict = {0:0,1:5,2:10,3:20,4:40,5:100,6:200}
    counter = 0
    x = input("Eingabe:")
    eingabeliste = x.split(' ')
    zahlen = len(eingabeliste)
    
    gewinnliste = []
    i=0
    while i < zahlen:
        random = [str(randint(0,49))]
        if (random not in gewinnliste):
            i +=1
            gewinnliste = gewinnliste + [str(randint(0,49))]

    for i in eingabeliste:
        if i in gewinnliste:
            counter +=1

    print('Gewinne:',gewinnliste)
    print('Geld:',dict[counter])

#lotto()


def ntobasetwo(n, c):
    binary = ''
    while n != 0:
        binary = binary + str(n%2)
        n = n//2

    #reverse the string
    binary = binary[::-1]

    #add c - len(binary) bits 
    if c > len(binary):
        binary = (c - len(binary) )*'0' + binary

    #cut c bits 
    binary = binary[:c]

    return binary

def complement(b):
    #kippe alle bits
    kippe = ''
    for i in b:
        if i == '0':
            kippe = kippe + '1'
        else:
            kippe = kippe + '0'

    #add 1
    zweierk = ''
    #go through the list from right to left
    for i in range(len(kippe)-1,-1,-1):
        if kippe[i] == '1':
            zweierk = '0' + zweierk
        else:
            zweierk = '1' + zweierk 
            #add the remaining string to zweierk
            zweierk = kippe[:i] + zweierk
            #stop the loop
            break

    return zweierk


def ztobasetwo(z, c):
    if z < 0:
        return complement(ntobasetwo(z*-1,c))
    else: 
        return ntobasetwo(z,c)



zahl = 5
c = 3
print("zahl:",zahl,"binary:",ztobasetwo(zahl,c),"complement:",ztobasetwo(zahl*-1,c))

