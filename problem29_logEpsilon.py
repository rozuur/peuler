# Assuming epsilon is 10**-10

from math import log
n = 10**10
R = xrange(2,101)
l = [ int(i*n*log(j)) for i in R for j in R]
m = set(l)
print len(m)

# One liner 
# print len( set( ( int(i*10**10*log(j)) for i in xrange(2,101) for j in xrange(2,101))))
