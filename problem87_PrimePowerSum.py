MAX = 50000000
MAX_SQUARE = int(MAX ** 0.5)
MAX_CUBE = int(MAX ** (1.0/3))
MAX_FOURTH = int(MAX ** 0.25)

end = MAX_SQUARE
sqrend = int(end**(0.5))
np = set(j for i in xrange(3,sqrend,2) for j in xrange(i*i,end,i+i))
p2 = set( i for i in xrange(3,end,2))
p2 = (p2 - np) ; p2.add(2)
p3 = [i**3 for i in p2 if i < MAX_CUBE]
p4 = [i**4 for i in p2 if i < MAX_FOURTH]
p2 = [i**2 for i in p2]

numbers = set()
for c in p4:
    for b in p3:
        for a in p2:
            n = a + b + c
            if n <= MAX:
                numbers.add(a + b + c)

print len(numbers)

