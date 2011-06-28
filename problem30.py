# If some number has all 9's then summing all fifth powers of 9 must be
# less than 10^n.If some numbers are changed, they will be less than 10^n

nPow5 = dict((i,i**5) for i in xrange(10))

# Get end of numbers to which iteration should be performed
length = 1
while length*nPow5[9] > 10**length:
    length += 1

def isfifthpower(n):
    nn, tn = 0, n
    while n:
        nn = nn + nPow5[(n%10)]
        n /= 10
    #    print "Fifth power of %d is %d"%(tn,nn)
    return nn==tn

s = [n for n in xrange(nPow5[2],10**length) if isfifthpower(n)] #since 1 should not be included, next is 2

print sum(s)

                    
