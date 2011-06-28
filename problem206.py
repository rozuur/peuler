from math import sqrt

sq = range(1,10)
start = "".join([ "%d0"%(i,) for i in sq ] + ['0'])
end = "".join([ "%d9"%(i,) for i in sq ] + ['0'])
print start,end

sq = "".join([str(i) for i in sq]+['0'])
start = int(sqrt(int(start)))
end = int(sqrt(int(end)))

print start,end,sq
for i in xrange(start,end+1,10):
    print str(i*i)[::2],sq,i

