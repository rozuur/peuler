m = 28123
def FactorSum(n):
    """Returns a list of elements with its factor sums"""
    l = [0]*n
    l[1] = 1
    for i in xrange(1,(n>>1)):
        for j in xrange(i+i,n,i):
            l[j] += i
    return l

def main(m = 28124):
    l = [ index for index,value in enumerate(FactorSum(m)) if value>index ]

    Ab = range(m)
    lenl = len(l)

    for i in xrange(lenl):
        num1 = l[i]
        for num2 in l[i:]:
            num = num1 + num2
            if num >= m:
                break
            Ab[num] = 0
        i += 1

    print sum(Ab)

if __name__=="__main__":
    main()

"""First Written for is fast
def main(m = 28124):
    l = [ index for index,value in enumerate(FactorSum(m)) if value>index ]

    Ab = range(m)
    i = 0
    lenl = len(l)

    while i < lenl:
        j = i
        k = l[i] + l[j]
        while k<m:
            Ab[k] = 0
            j += 1
            k = l[i] + l[j]
        i += 1

    print sum( Ab )
"""
