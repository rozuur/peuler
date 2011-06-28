"""
Initially attacked this problem like 3n+1 problem with dict.
Found that freq of cycle is not used in findchain and modified dict to set
But once output of repeated values is seen its clear that each value has all
its permutations
DataStructure : Set
Technique : Permutations
"""

from itertools import permutations

def numperms(n): # can have two sets, where each 0 replaced by 1
    def cat(x,y):
        return 10*x+y
    l = []
    while n != 0:
        l.append(n%10)
        n /= 10
    return set(reduce(cat,i) for i in permutations(l) if i[0] != 0) # all permutations are not valid as 0 also has factorial value
        
def findchain(i):
    chn = set()
    chi,n = 1,i
    vals = numperms(i)
    while i not in chn:
        chn.add(i)
        f = 0
        while i != 0:
            f += fact[i%10]
            i /=10
        chi+=1
        i = f
        #if i < 1000000 and i not in nums:  # No performance gain
        #    nums.update(numperms(i))
        if f in chn:
            break
    nums.update(chn)
    nums.update(vals) # should only be added here
    if chi - 1 == 60:
        #print vals
        return vals
    else:
        return set()

if __name__ == "__main__":        
    nums = set()
    fact = [1]
    nums.add(0)
    vals = set()
    for i in xrange(1,10):
        fact.append(fact[i-1]*i)
        nums.add(i)
    for i in xrange(10,1000000):
        if i % 100000 == 0:
            print i, len(nums)
        if i not in nums:
            vals.update(findchain(i))
    print len(vals)
