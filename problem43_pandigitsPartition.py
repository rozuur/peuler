"""
Very Clever approach
Read the bug code and understand
"""
def main():
    nums = {}
    for i in xrange(10,100):
        _i = str(i)
        if len(set(_i)) == 2 and '0' not in _i:
            nums[i] = "0"+_i
    for i in xrange(100,1000):
        _i = str(i)
        if len(set(_i)) == 3:
            nums[i] = _i
    P = (17,13,11,7,5,3,2)
    divby = [[nums[i] for i in xrange(n,1000,n) if nums.get(i,0)!=0] for n in P]
    print sum(panDigits(reduce(lambda x,y :Valid(y,x) ,divby)))


def Valid(first,second):
    temp = []
    for j in second:
        use = set(j)
        for i in first:
            if i[1:3] == j[0:2] and i[0] not in use:
                temp.append(i+j[2:])
    return temp

def panDigits(finalnums):
    nums = set("0123456789")
    s = []
    for i in finalnums:
        n = nums - set(i)
        n = [_n for _n in n][0]
        s.append(int(n+i))
    return s

def Usernjlytoh():
    divisors=[2,3,5,7,11,13,17]

    snum=set([0,1,2,3,4,5,6,7,8,9])

    def resetNum(num,i):
        for k in xrange(i):
            num[k]=-1
    def getSum(num=None,last=-1):
        if num==None:
            num=[-1 for i in range(10)]
        _sum=0
        if last==-1:
            for _last3 in xrange(17,1000,17):
                _plast=_last3
                resetNum(num,10)
                for i in xrange(3):
                    num[-i-1]=_plast%10;_plast=_plast/10;
                if len(set(num))<4:continue
                _sum+=getSum(num,-3)
        elif last>-9:
            prev=10*num[last]+num[last+1]
            resetNum(num,len(num)+last)
            for k in filter(lambda i:(100*i+prev)%divisors[last+1]==0,snum.difference(set(num))):
                num[last-1]=k
                _sum+=getSum(num,last-1)
        else:
            num[0]=snum.difference(set(num)).pop()
            _sum=reduce(lambda i,j:10*i+j,num)
        return _sum

    print getSum()

if __name__ == "__main__":
    from time import time
    t = time()
    main()
    s = time()
    Usernjlytoh()
    print time()-s,s-t

"""
#Find Bug in this code

from itertools import permutations
pandigits = set("0123456789")

numbers = {}
def lenOfUniq(num):
    return len(set(str(num)))

for i in xrange(10,100):
    if lenOfUniq(i) == 2:
        numbers[i] = "0"+str(i)

for i in xrange(100,1000):
    if lenOfUniq(i) == 3:
        numbers[i] = str(i)
 
div2 = [numbers[i] for i in xrange(0,1000,2) if numbers.get(i,0) != 0 ]
div3 = [numbers[i] for i in xrange(0,1000,3) if numbers.get(i,0) != 0 ]
div5 = [numbers[i] for i in xrange(0,1000,5) if numbers.get(i,0) != 0 ]
div7 = [numbers[i] for i in xrange(0,1000,7) if numbers.get(i,0) != 0 ]
div11 = [numbers[i] for i in xrange(0,1000,11) if numbers.get(i,0) != 0 ]
div13 = [numbers[i] for i in xrange(0,1000,13) if numbers.get(i,0) != 0 ]
div17 = [numbers[i] for i in xrange(0,1000,17) if numbers.get(i,0) != 0 ]

#Valid takes more time than Valid2, but this is not a bug, just observation
def Valid(first,second,debug=False): #Hint : Use debug 
    temp = set()
    for i in first:
        used = set(i)
        for j in second:
            if i[1:3] == j[0:2]:
                for x in j[2:]:
                    if x in used:
                        break
                else:
                    temp.add(i+j[2:])
    return temp

def Valid2(first,second):
    temp = set()
    for i in first:
        for j in second:
            used = set(j)
            if i[1:3] == j[0:2] and i[0] not in used:
                temp.add(i+j[2:])
    return temp

finalnums = reduce(lambda x,y : Valid(y,x) ,(div17,div13,div11,div7,div5,div3,div2))
finalnums2 = reduce(lambda x,y : Valid2(y,x) ,(div17,div13,div11,div7,div5,div3,div2))
print finalnums,finalnums2

s = 0
for i in finalnums:
    print i,
    n = pandigits - set(i)
    print n,
    n = [_n for _n in n][0]
    print n+i
    s += int(n+i)
print s

finalnums = reduce(lambda x,y : Valid(y,x) ,(div17,div13,div11,div7,div5,div3))
"""
