c, d = (input().split())

while(c != '0' or d != '0'):
    s = ''
    j = 0
    for i in range(len(d)):
        if(d[i] != c):
            s += d[i]
    
    if(s == ''):
        j = 0
    else:
        j = int(s)
        
    print(j)

    c, d = (input().split())