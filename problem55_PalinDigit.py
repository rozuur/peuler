def revnum(n):
    return int(str(n)[::-1])

def ispalin(n):
    return str(n) == str(n)[::-1]

def isLychrel(n):
    iter = 0
    while iter < 50:
        n = n + revnum(n)
        if ispalin(n):
            return False
        iter += 1
    else:
        return True

print len(filter(isLychrel, range(1, 10001)))
