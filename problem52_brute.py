# Or read cyclic numbers
i = 1
while 1:
    I = sorted(str(i))

    if sorted(str(2*i)) != I:
        i+=1
        continue

    if sorted(str(3*i)) != I:
        i+=1
        continue

    if sorted(str(4*i)) != I:
        i+=1
        continue

    if sorted(str(5*i)) != I:
        i+=1
        continue

    if sorted(str(6*i)) != I:
        i+=1
        continue

    print "Required Number is",i
    break
