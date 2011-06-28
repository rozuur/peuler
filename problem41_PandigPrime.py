np = set( ( j for i in xrange(3,10000,2) for j in xrange(i*i,100000000,i*2) ))
p = set( range(3,100000000,2) )
primes = ( str(i) for i in p.difference(np) )
