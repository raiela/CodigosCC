def maior(n, m):
    	tamN = len(n)
	tamM = len(m)
	maior = 0
	if(tamM >= tamN):
		return tamM
	return tamN


def somar(n, m):
	tamanhoN = len(n)-1
	tamanhoM = len(m)-1
	result = ""

	while tamanhoN > 1 and tamanhoM > 1:
		if(n[tamanhoN] == '1' and m[tamanhoM] == '1'):
			result += '0'
		else:
			aux1 = int(n[tamanhoN])
			aux2 = int(m[tamanhoM])
			s = aux1 + aux2
			result += str(s)

		tamanhoN -= 1
		tamanhoM -= 1

	if(tamanhoN >= tamanhoM):
		while tamanhoN >= 0:
			result += n[tamanhoN]
			tamanhoN -= 1
	elif(tamanhoN < tamanhoM):
		while tamanhoM >= 0:
			result += m[tamanhoM]
			tamanhoM -= 1
	

	return result[::-1]


while True:
	try:

		a,b = input().split()

		num1 = int(a)
		num2 = int(b)

		binario = somar(bin(num1), bin(num2))
		print(int(binario, 2))

	except EOFError:
		break