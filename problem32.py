s = set()
start = 1234
end = 9876
pan = set(str(123456789))
for i in xrange(2,int(end**(0.5))):
    for j in xrange(start/i,end/i):
        n = str(i)+str(j)+str(i*j)
        if len(n) != 9 or set(n) != pan:
            continue
        s.add(i*j)
print sum(s)
