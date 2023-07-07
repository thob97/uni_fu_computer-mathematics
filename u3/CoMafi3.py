def sieb(n):
	temp = [i for i in range(2,n+1)]
	length = len(temp)
	i = 0
	
	while i < length:
		j = i+1	
	
		while j < length:
			if temp[j]%temp[i] == 0:
				temp.remove(temp[j])
				length -=1
			j+=1
		i+=1
	return temp
	
#print(sieb(11))



#rundet zu - unendlich wenn negativ. rundet ab < -0.5 ab zu -1
#rundet zu + unendlich wenn prositiv. rundet ab > 0.5 auf zu 1
def runden(x,L):
	#tests if negative
	vorzeichen = 1
	if x < 0:
		vorzeichen = -1
		x *= -1
	
	#in gleitkommazahl darstellung bekommen
	counter = 0
	while x >= 1 and x!=0:
		x /= 10
		counter += 1
	
	while x < 0.1 and x!=0:
		x *= 10
		counter -=1
	
	#runden auf L Nachkommerstellen
	x = round(x, L)
	
	
	#in die normal form zurück bringen
	#schon hier können fehler wie folgt passieren: 0,123123 * 10**3 = 123,122999999, da der Bruch in Binär nicht endlich darstellbar ist.
	x = (x*10**counter)
	
	return x * vorzeichen
	


def add(x,y,rd):
	x = runden(x,L)
	y = runden(y,L)
	return runden(x+y,L)
	
def mult(x,y,rd):
	x = runden(x,L)
	y = runden(y,L)
	return runden(x*y,L)
	
def binomA(a, b, rd):
	a = rd(a,L)
	b = rd(b,L)
	c = add(a,b,rd)
	return mult(c,c,rd)
	
def binomB(a,b, rd):
	a = rd(a,L)
	b = rd(b,L)
	a2 = mult(a,a,rd)
	b2 = mult(b,b,rd)
	a2b = mult(2,mult(a,b,rd),rd)
	return add(a2,(add(a2b,b2,rd)), rd)

L=5
a = 0.012345 
b = -0.01234 
#print(runden(a,L))
#print(runden(b,L))
#print(add(a,b,runden))
#print(mult(a,b,runden))
#print(binomA(a,b,runden))
#print(binomB(a,b,runden))

for L in range(1,20):
    print("L:",L,"binomA:",binomA(a,b,runden),"binomB",binomB(a,b,runden))