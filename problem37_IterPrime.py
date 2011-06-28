sqrend = 1000
end = sqrend*sqrend
np = set(j for i in xrange(3,sqrend,2) for j in xrange(i*i,end,i+i))
p = set( i for i in xrange(3,end,2))
p = p - np
p.add(2)

def isTruncatablePrime(i):
    n = str(i)
    for i in xrange(1,len(n)):
        if int(n[i:]) not in p or int(n[:-i]) not in p:
            return False
    return True

s,t = 0,0

erase = set("1379")

for i in p:
    if set(str(i)[1:-1]) - erase : 
        continue
    if isTruncatablePrime(i):
        t += 1
        s += int(i)
        if t==15:
            break
        
print s - sum((2,3,5,7))

