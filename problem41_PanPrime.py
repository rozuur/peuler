"""
       ----
Sigma   >   9 or 8 is divisable by 7 
       ----
"""
from itertools import permutations
from math import sqrt
np = '245680' # not primes
l = [ int("7"+"".join(i)) for i in permutations('654321') if i[-1] not in np] #needs maximum first

for i in l:
    j = 3
    isprime = True
    while j <= sqrt(i):
        if i%j == 0:
            isprime = False
            break
        else:
            j += 2
    if isprime == True:
        print i
        break

