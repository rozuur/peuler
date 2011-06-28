def noOfFactors(end = 1000000):
    fc = [ (i+1)&1 for i in xrange(end)]
    l = []
    for i in xrange(3,end,2):
        if fc[i] == 0:
            for j in xrange(i+i,end,i):
                fc[j] += 1
        if fc[i] == fc[i-1] == fc[i-2] == 4:
            l.append(i)

    for i in l:
        if fc[i] == fc[i+1]:
            print i
            break
    

if __name__ == "__main__":
    noOfFactors()
            
