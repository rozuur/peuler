stop = 10000
l = [ i for i in xrange(1,stop) ]
divsum = [0]

for i in l:
    ssum = 0
    for j in xrange(1,i/2 + 1):
        if i%j == 0:
            ssum += j
    divsum.append(ssum)

print divsum[220]

problem21 = 0
for i in xrange(1,stop):
    if divsum[i]<stop:
        if i == divsum[divsum[i]] and i!=divsum[i]:
             problem21 += i

print problem21
