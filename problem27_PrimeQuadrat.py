"""
Let no of primes be > 40
Hence 1600 + 40 * a  + b must be a prime for some value of a and b
So maximum primes will be less than 1600 + 40*1000 + 1000

"""
def main():
    m = 42600 # 1600 + 40000 + 1000
    sm = int(m**0.5)
    np = set( j for i in xrange(3,sm,2) for j in xrange(i*i,m,i+i))
    p = set(i for i in xrange(3,m,2))
    p = p - np
    p.add(2)
    pless1000 = set( i for i in xrange(3,1000,2))
    pless1000 = pless1000 - np
    pless1000.add(2)

    maxa = maxb = maxc = 0
    c = 0
    for a in xrange(-999,1000):
        for b in pless1000:
            if 1+a+b not in p:
                continue
            c = 2
            for n in xrange(2,100):
                if (n*(n+a)+b) in p:
                    c += 1
                    if c>maxc and b<1000:
                        maxc = c
                        maxa = a
                        maxb = b
                else:
                    break

    print maxc,maxa,maxb,maxb*maxa

if __name__ == "__main__":
    main()
