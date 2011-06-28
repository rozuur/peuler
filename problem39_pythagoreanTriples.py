"""2m(m+n) <=1000
m(m+n) <=500
m< sqrt(500) and n<m """

from fractions import gcd

l = [0]*1001
 
mend = int(500**0.5)

for m in xrange(2,mend):
    for n in xrange(1,m):
        x = 2*m*(m+n)
        y = x
        while y<=1000:
            if gcd(m,n) == 1: # If k*(m,n) can lead to y,5(2,1) and not 10,2
                l[y] += 1
            y = y + x

maxl = max(l)
s = [i for i,j in enumerate(l) if j == maxl]
print s,maxl,l[840],l[720]
