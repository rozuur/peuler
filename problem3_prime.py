def primes(n):
    # Generator for primes < n
    yield 2
    # Sieve of composite numbers
    odd_composites = set(i*j for i in xrange(3,n,2) for j in xrange(i,n,2))
    for i in xrange(3,n,2):
        if i not in odd_composites:
            yield i

def factors(n):
    # Returns factors in ascending order
    return tuple(i for i in primes(int(n**0.5)+1) if n % i == 0)

num = 600851475143
print factors(num)[-1]

factors = tuple(i for i in xrange(3,int(num**0.5)+1,2) if num % i == 0)
from fractions import gcd
for i in xrange(len(factors)):
    if all(gcd(factors[i],fact) == 1 for fact in factors[:i]):
        print factors[i]
        
    
    
