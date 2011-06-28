def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

i = 134043
while i<134044:
    for x in xrange(i,i+4):
        count = 0
        firstbreak = False
        for y in xrange(x+1,i+4):
            print "Finding gcd(%d,%d) = %d"%(x,y,gcd(x,y))
            if gcd(x,y) == 1:
                count = count + 1
    if count == 6:
            break
    i = i + 1
    print i,

print i
