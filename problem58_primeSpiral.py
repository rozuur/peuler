
"""
Initially tried to solve by sieve. Which was time consuming, why?

Sequence of all diagnonal numbers
4*n*n-10*n+7 S-6n+6
4*n*n-6*n+3  S-2n+2
4*n*n-4*n+1  S
4*n*n-8n+5   S-4n+4
S,N = (2*n-1)**2, n-1
"""
from math import sqrt

def isprime(n):
    for i in xrange(3,int(sqrt(n)),2):
        if n%i == 0:
            return 0
    return 1

diagPrimes = 0
for i in xrange(2,1000000):
    S = (2*i-1)**2
    N = (i-1)
    diagPrimes += isprime(S-2*N)
    diagPrimes += isprime(S-4*N)
    diagPrimes += isprime(S-6*N)
    if diagPrimes*100 / (4*i-3) < 10:
        print 2*i-1
        break

