# Take log's 
from math import log
import sys

def f(s):
    a,b = s.strip().split(",")
    a,b = int(a),float(b)
    return b*log(a)

l = sys.stdin.readlines()
s = [ (f(j),i,j) for i,j in enumerate(l)]

m = max(s)

print m[1]+1,m[2]
