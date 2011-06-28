from math import sqrt
def main():
    m = 10000
    sm = int(sqrt(m))
    np = set( j for i in xrange(3,sm,2) for j in xrange(i*i,m,i+i))
    p = set(i for i in xrange(1001,m,2)) # since all number are 4 digits
    p = p - np

    rest = set([])
    numbers = []
    for i in p:
        rest.add(i)
        for j in p-rest:
            if (i+j)/2 in p:
                k = (i+j)>>1
                if set(str(i)) == set(str(j)) == set(str(k)) :
                    numbers.append( [i,j,k] )
    for i in numbers:
        if 1487 not in i:
            print "".join(map(str,(sorted(i))))
if __name__ == "__main__":
    main()
