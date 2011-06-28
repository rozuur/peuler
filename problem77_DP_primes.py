def sieve(n):
    # Generator for primes < n
    yield 2
    # Sieve of odd composite numbers
    odd_composites = set(i*j for i in xrange(3,n,2) for j in xrange(i,n / i + 1,2))
    # yields all odd primes < n
    for i in xrange(3,n,2):
        if i not in odd_composites:
            yield i

counts = [0,0,0,0] # 0,1,2,3

def f(n):
    count = 0
    count1 = 0
    count2 = 0
    primes = set(sieve(n))
    for p in primes:
        c = 0
        if n - p >= 2:
            if counts[p] == 0:
                c = counts[n - p] if counts[n - p] else 1
            else:
                c = counts[p] * (counts[n - p] if counts[n - p] else 1)
        if n - p in primes and n - p != p:
            count2 += c
        else:
            count1 += c
    count = count1 + count2 / 2
    counts.append(count)
    print n, count

for i in xrange(4,62):
    f(i)




