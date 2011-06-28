class Fraction:
    # Class which represents fraction for continued fraction
    
    def __init__(self,r):
        self.r = r
        self.n = 0
        self.d = 1
        self._r = int(self.r ** 0.5)
        self.a = 0

    def next(self):
        a = int((self._r + self.n) / self.d)
        self.a = a
        # Subtracting a from fraction
        # print "Before subtraction", self.r, self.n, self.d
        self.n = self.n - self.d * a
        # print "After subtraction", self.r, self.n, self.d
        self._inverse()
        # print "After inverse", self.r, self.n, self.d
        return self.a, self.n, self.d

    def _inverse(self):
        den = self.r - self.n * self.n
        mod = den % self.d
        if mod:
            raise "Data Representation Exception"
        self.n = -self.n
        self.d = den / self.d

    def convergents(self):
        stop = self.next()[1:]
        yield self.a
        while True:
            curr = self.next()[1:]
            yield self.a
            if curr == stop:
                break

if __name__ == "__main__":
    import time
    begin = time.time()
    # Problem 64
    count = 0
    for i in xrange(2,10000):
        S = Fraction(i)
        stop = S.next()[1:]
        period = 1
        while True:
            try:
                f = S.next()
            except ZeroDivisionError:
                break
            if f[1:] == stop:
                if period % 2:
                    count += 1
                #print i, period
                break
            else:
                period += 1
    print count, time.time() - begin





