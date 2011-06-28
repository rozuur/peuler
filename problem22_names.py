l = raw_input()
l = list(eval(l))

val = range(ord('A'),ord('Z')+1)
dval = zip(map(chr,val),range(1,1+ord('Z')-(ord('A')-1)))
dval = dict(dval)

out = 0

for i in xrange(len(l)):
    s=0
    for j in l[i]:
        s = s + dval[j]
    out = out + i*s
print out

#or we can use reduce
#reduce( lambda x, y: x + y, [ reduce( lambda x, y: x + y, [ ( j + 1 ) * ( ord( i ) - 64 ) for i in x[ j ] ] ) for j in xrange( len( x ) ) ] )

