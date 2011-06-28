np = set( ( j for i in xrange(3,1000,2) for j in xrange(i*i,1000000,i*2) ))
p = set( range(3,1000000,2) )
primes = ( str(i) for i in p.difference(np) )

tpri = [ i for i in primes if not ('2' in i or '4' in i or '5' in i or '6' in i or '8' in i or '0' in i ) and len(i)>2]

cpri=[]
n = 0
for i in tpri:
    j = len(i)
    c = 0
    while j:
        i = i[-1]+i[:-1]
        if i in tpri:
            c += 1
        j = j - 1
    if c == len(i):
        cpri.append(int(i))
        n += 1

cpri.sort()
print n+13
    
