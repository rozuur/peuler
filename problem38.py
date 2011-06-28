"""
"x" + "2*x" <= "987654321"
clearly len(x) < 4

since pandigit should be maximum and must beat given test case 918273645 we can
assume that it presents when 'x' start with 9

Observe: 9[0-9] will have too few or too many digits (8 or 11) 
Observe: 9[0-9][0-9] wiil have too few or too many digits (7 or 11) 
Observe: larger than 100000 won't work, too few or too many digits. 

Conclusion: 
The candidate starting number must be in the 9[0-9][0-9][0-9] series. 

"""
Digs = 987654321
end = 9876
panDigs = set(str(Digs))
l = []

for n in xrange(9182,end):
    s = str(n)
    i = 2
    while len(s) < 9:
        s += str(i*n)
        i += 1
    if set(s) == panDigs and len(s) < 10:
        l.append(s)

print max(l)
