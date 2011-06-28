import time
tstart = time.time()

C=[[0 for i in range(51)] for i in range(51)]

for i in range(51):
    C[i][0]=C[i][i]=1

def nCr(n,r):
    if C[n][r] == 0 :
        C[n][r] = nCr(n-1,r) + nCr(n-1,r-1)
        C[n][n-r] = C[n][r]
    return C[n][r]
    
for i in range(51):
    nCr(50,i)
    
def squarefree(n):
    if n%4 == 0 or n%9 ==0 or n%25 == 0 or n%49 == 0:
        return 0
    i=11
    while i*i<=n:
        if n%(i*i) == 0:
            return 0
        i=i+2
    return 1

s=0
for i in range(51):
    print i,i/2+1,len( filter(lambda x: x!=0,C[i]) )
    for j in range (i>>1) + 1:
        if squarefree(C[i][j]) :
            s=s+C[i][j]


print s, time.time()-tstart
