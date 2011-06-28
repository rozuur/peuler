""" Considering mean value of each digit in n**a is 5 when one digit in n is 9
    also n^a is increases when n inc and a inc 
    we can assume that, when n and a varies in [90-100] we have max sum
"""
max=0
for i in range(90,101):
    x=i**89    
    for j in range(90,101):
        x=x*i
        s = sum([ int(k) for k in str(x)])
        if s>max:
            max=s
            a,b=i,j
print a,b,max










