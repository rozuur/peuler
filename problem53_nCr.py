#can also use stirlig formulae
import time
tstart = time.time()

C=[[0 for i in range(101)] for i in range(101)]

for i in range(101):
    C[i][0]=C[i][i]=1

def nCr(n,r):
    if C[n][r] == 0 :
        C[n][r] = nCr(n-1,r) + nCr(n-1,r-1)
        C[n][n-r] = C[n][r]
    return C[n][r]

if __name__ == "__main__":
    
    for i in range(101):
        nCr(100,i)
    
    s=0
    for i in range(101):
        t = filter(lambda x: x>1000000,C[i])
        s = s + len(t)
    print s, (time.time()-tstart)
    

