"""
phi(n) = n(1-1/p)(1-1/q).. where p,q... are prime factors of n
n/phi(n) will be maximum if it has maximum prime factors so for a
given n multiply all primes such that resulting multiplied number is
maximum and <= n
"""

import sys

noprime = [j for i in xrange(2,11) for j in xrange(i*i,110,i)]
p = [x for x in range(2,110) if x not in noprime]
p.insert(0,1)

pm=[reduce(lambda x,y:x*y,p[:i],1) for i in xrange(1,len(p))]
pm.insert(0,0)

inp = sys.stdin.readlines()
inp = [int(i) for i in inp]

for number in inp:
	for i in xrange(1,len(pm)):
		if pm[i-1] < number <= pm[i]:
			if number == pm[i]:
				print number
			else:
				print pm[i-1]
			break
