# If some number has n 9's then summing all of 9! is n*9!, which must be
# less than 10^n.If some numbers are changed, they will be less than 10^n

Fact = {}
Fact[0] = 1
for i in xrange(1,10):
    Fact[i]=Fact[i-1]*i

# Get end of numbers to which iteration should be performed
length = 1
while length*Fact[9] > 10**length:
    length += 1

def digitFactorialSum(n):
    nn, tn = 0, n
    while n:
        nn = nn + Fact[(n%10)]
        n /= 10
    #    print "Fifth power of %d is %d"%(tn,nn)
    return nn==tn

s = [n for n in xrange(10,length*Fact[9]) if digitFactorialSum(n)] #since 1 should not be included, next is 2

print sum(s)

