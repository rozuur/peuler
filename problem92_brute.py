sqs = {}
for i in xrange(10):
    sqs[i] = i*i
numend = {1:1,89:89}
c = 0
for n in xrange(1,10000000):
    if n % 1000000 == 0:
        print n
    if numend.has_key(n):
        if numend[n] == 89:
            c += 1
        continue
    end = n
    nums = []
    while end != 1 and end != 89 and numend.has_key(end)==False:
        nums.append(end)
        i,end = end,0
        while i != 0:
            end += sqs[i % 10]
            i /= 10
    for m in nums:
        numend[m] = numend[end]
    if numend[n] == 89:
        c += 1

print c
