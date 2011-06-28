def sumOfDigits(n):
    print n
    s = 0
    while n:
        print n%10 ,
        s += (n%10)
        n /= 10
    return s

l = []
for i in xrange(1,34):
    l.extend([i<<1,1,1])

h2,h1,k2,k1 = 2,3,1,1
j = 2
for i in l:
    h           = h1*i+h2
    k           = k1*i+k2
    h2,h1,k2,k1 = h1,h,k1,k
    j = j + 1
    if j == 100:
        break


print sumOfDigits(h)

