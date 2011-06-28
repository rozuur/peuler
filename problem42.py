trinum = [(i*i+i)>>1 for i in xrange(25)]  
l = raw_input() 
l = eval(l) # since we have read string representation of list
aval = ord('A')
def values(x):
    ss = 0
    for i in x:
        ss += ord(i)-aval+1
    return ss

print "No of triangle numbers are",
print len([i for i in map(values,l) if i in trinum])
