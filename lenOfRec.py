def lenOfRec(denom):
    """ Length of non terminating decimal in 1/n """
    d = denom
    n = 1 #numerator
    count = 0
    while n!=0:
        n = n*10 % d
        count += 1
        if n == 1:
            break
        
    return count

if __name__ == "__main__":
    l = []
    for i in xrange(0,100,10):
        l = l + [i+1,i+3,i+7,i+9]
        
    l = [lenOfRec(i) for i in l]
    print "Maximum non terminating decimal length is %d"%( max(l) ,)
