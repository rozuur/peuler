from fractions import gcd

p = []

def ffractions(i,j):
    a = i*10+j
    for y in xrange(i,j):
        if y == i: continue
        n = j*10+y
        if a*y == i*n:
            g = gcd(a,n)
            p.append((a/g,n/g,g))
        n = y*10+j
        if a*y == i*n:
            g = gcd(a,n)
            p.append((a/g,n/g,g))

for i in xrange(1,10): 
    for j in xrange(i+1,10):
        ffractions(i,j)

den,num = 1,1
for i in p:
    print "Fraction %d/%d Gcd = %d"%(i[0],i[1],i[2])
    den *= max(i[:-1])
    num *= min(i[:-1])

print den/num
