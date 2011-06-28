from math import sqrt

def factorsOfSquare(n):
    c = 0
    i = 2
    sn = n*n
    while i<sn:
        if sn%i == 0:
            c += 1
        i += 1
    
    print n,c
    return c + 1

i = 2
while factorsOfSquare(i) < 1000:
    i += 2
else:
    print i
        
