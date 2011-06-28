""" Non brute solution is related to finding patterns of terms for whicn num>den

continued fraction of two is in form 
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

1 + 1/ 1 + 1
1 + 1/(1 + 3/2)
1 + 1/(1 + 7/5)
1+1/(1+a/b) = a+2b/a+b

appending term should be d+b/d  d = a+b
"""
from math import log
def f(end):
    l = [(3,2)]
    for i in xrange(end):
        d = l[-1][0]+l[-1][1]
        l.append( (d+l[-1][1],d) )
    lval=[1 for x,y in l if int(log(x,10))>int(log(y,10))]
    sval=[1 for x,y in l if len(str(x))>len(str(y))]
    print len(lval),len(sval)
    
if __name__ == "__main__":
    f(1000)
