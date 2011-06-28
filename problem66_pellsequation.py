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

    # Problem 66 Pell's equation
    max_x = 9
    D = 5
    nums = xrange(9,1001)
    for n in nums:
        S = Fraction(n)
        try:
            convs = list(S.convergents())
            if len(convs) % 2 == 0:
                # http://mathworld.wolfram.com/PellEquation.html  (28)
                convs = convs + convs[1:-1]
        except ZeroDivisionError:
            continue
        # print convs
        p,q = convs[0],1
        # print n,(p,q)
        sol = r,s = p*convs[1] + 1, convs[1]
        # print n,sol
        convs = convs[2:]
        if convs:
            for c in convs:
                r,s,p,q = c*r + p, c*s+q, r, s
                sol = r,s
                # print n,sol
        if sol[0] > max_x:
            max_x = sol[0]
            D = n
            print n,sol,len(convs)

        



