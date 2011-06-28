"""
x^n has n digits if
10^(n-1) <= x^n < 10^n 
So x < 10
n-1 <= n*log10(x) < n
"""
l = []
for i in xrange(1,10):
    j = 1
    while j-1 <= j*log(i,10) <= j:
        print i**j
        j += 1
        l.append(i**j)

print sum(l)
