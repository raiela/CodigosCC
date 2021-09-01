cont = 1

n,q = map(int, input().split())
while(q != 0 or n !=0 ):
	marmore = []

	for i in range(n):
		m = int(input())
		marmore.append(m)

	marmore.sort()
	dicM = {}
	aux = 1
	aux2 = -1
	for i in marmore:
		if(i not in dicM.keys()):
			dicM[i] = aux
		else:
			dicM[aux2] = i
			aux2 -= 1
		aux += 1
	
	print("CASE# "+str(cont)+":")
	for i in range(q):
		c = int(input())
		if(c not in dicM.keys()):
			print(c, "not found")
		else:
			print(c, "found at", dicM[c])

	cont += 1
	n,q = map(int, input().split())