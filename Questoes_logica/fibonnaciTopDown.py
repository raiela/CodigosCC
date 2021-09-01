cont = 0
ind = 0
conts = {0:1, 1:1, 2:2, 3:4,4:8}
varAux = 0

def chamadas(n):
    if (n in conts):
        return conts[n]
    aux = 0
    for i in range(4, n+1):
        if(i not in conts.keys()):
            aux = conts[i-1]+conts[i-2]+2
            conts[i] = aux
    return conts[n]

def fibonacciTopDown(n, table = {}):
    if n == 1 or n == 0:
        return n
    try:
        return table[n]
    except:
        table[n] = fibonacciTopDown(n-1) + fibonacciTopDown(n-2)
        return table[n]

    
n = int(input())
for i in range(n):
    cont = 0
    number = float(input())
    aux = fibonacciTopDown(number)
    print("fib(%.0f) = %d calls = %.0f"%(number, chamadas(int(number)), aux))