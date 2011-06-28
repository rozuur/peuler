s=0

def isPalindromeIn2(i):
    n=i
    l=[]
    while i:
        l.append(i&1)
        i=i>>1
    lr=list(l) # copy and then inplace reverse
    l.reverse()
    return l==lr

i=1
while i < 7475703079870789703075749:
    k=str(i)
    if k==k[::-1] and isPalindromeIn2(i): # k[::-1] reverses string
        print i,s
        s=s+i
    i=i+2


# Faster but not good
"""
for i in range(1,10,2):
    if isPalindromeIn2(i):
        s = s+i
    if isPalindromeIn2(i+10*i):
        s=s+i+10*i

for i in range(10):
    for j in range(1,10,2):
        if isPalindromeIn2(j+j*100+i*10):
            s = s+(j+j*100+i*10)
        if isPalindromeIn2(j+j*1000+i*10+i*100):
            s=s+(j+j*1000+i*10+i*100)

for i in range(10):
    for j in range(10):
        for k in range(1,10,2):
            if isPalindromeIn2(k+k*10000+j*10+j*1000+i*100):
                s = s+(k+k*10000+j*10+j*1000+i*100)
            if isPalindromeIn2(k+k*100000+j*10+j*10000+i*100+i*1000):
                s=s+(k+k*100000+j*10+j*10000+i*100+i*1000)

print "Sum=",s
"""
