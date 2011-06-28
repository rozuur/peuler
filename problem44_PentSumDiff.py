import time
def pent():
    i = 1
    while True:
        yield i*(3*i-1)>>1
        i += 1

def ispent(n):
    _tmp=(1.0+(1.0+24.0*n)**.5)/6.0
    return _tmp==int(_tmp)



def f():
    l = set()
    c = 0
    for i in pent():
        #print c
        l.add(i)
        for j in pent():
            if j>=i:
                break
            if i-j in l:
                if ispent(i+j) is True:
                    print i,j,i-j
                    return
        c += 1

def g():
    """
    Pa-Pb=Px Pa+Pb = Py
    Py+Px = 2Pa
    Py-Px = 2Pb
    """
    l = set()
    for Py in pent():
        l.add(Py)
        for Px in pent():
            if Px >= Py:
                break
            if (Py-Px)>>1 in l and (Py+Px)>>1 in l:
                print Px
                return
        
    
ft = time.time()
f()
gt = time.time()
g()
print time.time()-gt,gt-ft
